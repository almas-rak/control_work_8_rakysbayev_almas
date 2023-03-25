from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from reviews.models import Product


class FormProduct(forms.ModelForm):
    product_name = forms.CharField(
        validators=(
            MinLengthValidator(limit_value=5, message='Введите хотя бы 5 символов'),
            MaxLengthValidator(limit_value=100,
                               message='Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов')
                    ),
        label='Название'
    )

    class Meta:
        model = Product
        fields = ('product_name', 'product_category', 'product_description', 'product_image')
