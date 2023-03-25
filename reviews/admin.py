from django.contrib import admin
from django.utils.safestring import mark_safe

from reviews.models import Product, Review


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_category', 'product_image', 'get_image')
    list_editable = ('product_name', 'product_category', 'product_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.product_image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_names', 'get_review_author', 'review_grade',)
    list_editable = ('review_grade',)

    def get_product_names(self, obj):
        return "\n".join([p.product_name for p in obj.review_product.all()])

    get_product_names.short_description = 'Продукты'

    def get_review_author(self, obj):
        return "\n".join([a.username for a in obj.review_author.all()])

    get_review_author.short_description = 'Авторы'


admin.site.register(Review, ReviewAdmin)
