
from django.shortcuts import render
from .models import Product
from . import views

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

