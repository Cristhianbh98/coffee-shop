from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from products.forms import ProductForm
from products.models import Product


# Create your views here.
class ProductFormView(FormView):
    template_name = "products/form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"