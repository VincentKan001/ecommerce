from django.shortcuts import render, redirect
from .models import Product
from .forms import NewProduct


# Create your views here.
def catalog(request):
    all_products = Product.objects.all();
    return render(request, 'shop/catalog.html',{
        'all_products':all_products
    })
    
def add_product(request):
    entry_form = NewProduct()
    return render(request, 'shop/add_product.html',{
        'form' : entry_form
    })
    # return render(request, 'shop/add_product.html')