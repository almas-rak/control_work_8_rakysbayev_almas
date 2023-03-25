from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    review_author = models.ManyToManyField(
        to=User,
        related_name='review_author',
        verbose_name='Автор'
    )

    review_product = models.ManyToManyField(
        to='reviews.Product',
        related_name='review_product',
        verbose_name='Продукт'
    )

    review_text = models.TextField(
        verbose_name='Отзыв'
    )

    review_grade = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(5)),
        verbose_name='Оценка'
    )
