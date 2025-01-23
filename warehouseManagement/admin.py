from django.contrib import admin
from .models import Product, Warehouse, Category, Transaction

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Category)
admin.site.register(Transaction)
