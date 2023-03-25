from django.contrib import admin

from reviews.models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_category', 'product_image')
    list_editable = ('product_name', 'product_category', 'product_image')


admin.site.register(Product, ProductAdmin)
