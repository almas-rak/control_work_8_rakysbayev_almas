from django.urls import path

from reviews.views import ListProduct

urlpatterns = [
    path('', ListProduct.as_view(), name='index'),
]
