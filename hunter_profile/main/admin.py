from django.contrib import admin

from hunter_profile.main.models import (
    Category, Product, Image
)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'description','slug')
    prepopulated_fields = {"slug":('name',)}
    #readonly_fields = ['slug']


class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'name', 'description','price', 
        'category', 'misc'
    )
    prepopulated_fields = {"slug":('name',)}
    #readonly_fields = ['slug']


class ImageAdmin(admin.ModelAdmin):
    list_display=(
        'title', 'product_photo',
    )
    readonly_fields=['product_photo']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
