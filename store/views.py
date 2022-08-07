from django.shortcuts import render
from .models import *

def home(request):
    context = {}
    return render(request, 'home.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'shop.html', context)

def product(request):
    query = request.GET.get('id')
    product = Product.objects.filter(id=query)
    context = {'products':product}
    return render(request, 'detail.html', context)