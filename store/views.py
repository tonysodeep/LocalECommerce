from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'store/index.html', context)


def about(request):
    return render(request, 'store/about.html', {})


def login_user(request):
    #check casesensitive
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message="You have been login")
            return redirect('home')
        else:
            messages.success(request, message="There a error please try again")
            return redirect('login')
    else:
        return render(request, 'store/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, message="you have be logout")
    return redirect('home')
