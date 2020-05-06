from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    # Product.objects.filter()
    # Product.objects.get()  # For getting a single product
    # Product.objects.save() #Inserting a new product or updating one
    # return HttpResponse('Hello World')
    return render(request,'index.html',{'products':products})


def new(request):
    return HttpResponse('New Products')
