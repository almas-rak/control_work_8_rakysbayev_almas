from django.views.generic import ListView

from reviews.models import Product


class ListProduct(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-id')
