from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from reviews.forms import FormProduct
from reviews.models import Product


class ListProduct(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-id')


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    form_class = FormProduct

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.pk})


class DetailProduct(DetailView):
    template_name = 'detail_product.html'
    context_object_name = 'product'
    model = Product


class UpdateProduct(UpdateView):
    template_name = 'update_product.html'
    model = Product
    form_class = FormProduct

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.pk})
