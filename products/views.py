from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response

from products.forms import ProductForm
from products.models import Product
from .serializers import ProductSerializer


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

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, _):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
