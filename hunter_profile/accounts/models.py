from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (AbstractBaseUser,
      BaseUserManager,PermissionsMixin)
from django.core.mail import send_mail


class HunterUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_reset_code(self, email):
        """
        Generates a new password reset code returns user
        """

        try:
            user = self.get(email__iexact=email)
            user.reset_code = self.make_random_password(length=20)
            user.reset_code_expire = timezone.now() + timedelta(days=2)
            user.save()

            return user

        except get_user_model().DoesNotExist:
            raise Exception('We can\'t find that email address, sorry!')
    
    def reset_password(self, user_id, reset_code, password):
        """
        Set new password for the user
        """

        if not password:
            raise Exception('New password can\'t be blank.')

        try:
            user = self.get(id=user_id)
            if not user.reset_code or user.reset_code != reset_code or user.reset_code_expire < timezone.now():
                raise Exception('Password reset code is invalid or expired.')

            # Password reset code shouldn't be used again
            user.reset_code = None
            user.set_password(password)
            user.save()

        except get_user_model().DoesNotExist:
            raise Exception('Password reset code is invalid or expired.')

    def change_password(self,user,current_password, password):
        """
        Updates user's current password
        """

        if not password:
            raise Exception('New password can\'t be blank.')

        # Changing user's password if old password verifies
        user = self.get(id=user.id)

        if not user.check_password(current_password):
            raise Exception('Your current password is wrong.')

        user.set_password(password)
        user.save()        



class HunterUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    reset_code = models.CharField(max_length=512, blank=True, null=True,
                                  help_text='Password reset code.', editable=False,default='')
    reset_code_expire = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    
    objects = HunterUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

