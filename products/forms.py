from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    description = forms.CharField(label="Descripción", max_length=300)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        data = self.cleaned_data
        product = Product.objects.create(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            available=data["available"],
            photo=data["photo"],
        )
        return product
