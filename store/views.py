from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'store/index.html', context)


def about(request):
    return render(request, 'store/about.html', {})
