from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'cart/index.html', {"cart_products": cart_products})


def cart_add(request):
    # get cart
    cart = Cart(request)
    # test for POST
    if (request.POST.get('action') == 'post'):
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # look up
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product)
        # get cart quantity
        cart_quantity = cart.__len__()

        # return respose
        # respose = JsonResponse({
        #     'Product Name': product.name
        # })
        respose = JsonResponse({
            'qty': cart_quantity
        })
        return respose
    return


def cart_update(request):
    return


def cart_delete(request):
    return
