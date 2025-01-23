
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'warehouse', 'cost_price', 'selling_price', 'quantity', 'expiry_date']  # Ensure 'quantity' is included if it's in the model
