from django.conf import settings
from hunter_profile.main.models import Category

def product_categories(request):
    """
    Returns a context variable containing categories with products
    """
    categories = [cat for cat in Category.objects.all()
                  if cat.products.count() > 0]
    return {'product_categories': categories}
