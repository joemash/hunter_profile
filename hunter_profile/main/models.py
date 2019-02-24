from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.db import models


class Category(models.Model):
    """Represents the Category of a Product on Sale"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents an Individual Product on Sale"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
            Category, on_delete=models.PROTECT,
            related_name='products',
            )

    misc = models.TextField(
        blank=True,
        help_text='Additional info about the product')
    added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Specification(models.Model):
    """Represents the Product Details"""

    title = models.CharField(max_length=50)
    details = models.TextField()
    product = models.ForeignKey(
            Product, on_delete=models.PROTECT,
            related_name='specs'
            )

    def __str__(self):
        return self.title


class Image(models.Model):
    """Represents an Image associated with the Product"""

    title = models.CharField("Image Name (optional)",
                             max_length=200, blank=True)
    photo = models.ImageField(upload_to='uploads')
    product = models.ManyToManyField(Product, related_name='images')

    def __str__(self):
        try:
            public_id = self.photo.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

    def product_photo(self):
        return mark_safe("<img border='0' alt='' src='/media/%s' height='50' />" % (self.photo.name))
    product_photo.short_description = 'Image'
