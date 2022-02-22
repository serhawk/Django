from django.shortcuts import render
from django.http import HttpResponse
from .models import product,category

def index(request):
    return render(request, "index.html")
def product1(request):
    return render(request, "product.html")
def about(request):
    return render(request, "about.html")
def testimonial(request):
    return render(request, "testimonial.html")
def contact(request):
    return render(request, "contact.html")

def products_list(request):
    products= product.objects.all()
    context={
        'products':products
    }
    return render(request,'product2.html',context)

# Create your views here.
