from django.shortcuts import render

# Create your views here.


def cart_summary(request):
    return render(request, 'cart/index.html', {})


def cart_add(request):
    return


def cart_update(request):
    return


def cart_delete(request):
    return
