from django.shortcuts import render
from .models import *

def index(request):
    computer = Mobile.objects.all()
    cards = Cards.objects.all()
    categoryes = Category.objects.all()

    return render(request,'index.html',{'computer':computer,'cards':cards,'categoryes':categoryes})

def only_cat_product(request,id):
    products = Laptop.objects.filter(category_id=id)
    return render(request,'only_cat_product.html',{'products':products})
