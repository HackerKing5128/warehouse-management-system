from django.shortcuts import render, redirect
from .models import Product, Category, Warehouse, Transaction
from .forms import ProductForm


def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})




def add_transaction(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        transaction_type = request.POST['transaction_type']
        Transaction.objects.create(
            product=product, quantity=quantity, transaction_type=transaction_type
        )
        return redirect('product_list')
