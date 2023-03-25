from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    CATEGORY_1 = 'Category_1', 'Категория_1'
    CATEGORY_2 = 'Category_2', 'Категория_2'
    CATEGORY_3 = 'Category_3', 'Категория_3'


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    product_category = models.CharField(
        verbose_name='Категория',
        max_length=15,
        choices=CategoryChoice.choices,
        default=CategoryChoice.CATEGORY_1
    )

    product_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    product_image = models.ImageField(
        upload_to='product',
        default='default/placeholder.png',
        verbose_name='Картинка'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product_name
