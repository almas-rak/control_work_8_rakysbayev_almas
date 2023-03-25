from django.urls import path

from reviews.views import ListProduct, CreateProduct, DetailProduct, UpdateProduct

urlpatterns = [
    path('', ListProduct.as_view(), name='index'),
    path('create/product/', CreateProduct.as_view(), name='create_product'),
    path('detail/product/<int:pk>', DetailProduct.as_view(), name='detail_product'),
    path('update/product/<int:pk>', UpdateProduct.as_view(), name='update_product'),
]
