from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_qty()
    cart_totals_prices = cart.cart_total()
    return render(
        request,
        'cart/index.html',
        {
            "cart_products": cart_products,
            'quantities': quantities,
            'total_prices': cart_totals_prices
        }
    )


def cart_add(request):
    # get cart
    cart = Cart(request)
    # test for POST
    if (request.POST.get('action') == 'post'):
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # look up
        product = get_object_or_404(Product, id=product_id)
        # save to session
        if cart.add(product, quantity=product_qty):
            respose = JsonResponse({}, status=200)
            messages.success(request, message="Item is added to cart...")
        else:
            respose = JsonResponse({}, status=200)
            messages.success(request, message="Item is already in cart")
        # return respose
        # respose = JsonResponse({
        #     'Product Name': product.name
        # })
        return respose
    return


def cart_update(request):
    cart = Cart(request)
    if (request.POST.get('action') == 'post'):
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product_id, product_qty)
        respose = JsonResponse({}, status=204)
        messages.success(request, message="Your cart have been updated... ")
        return respose


def cart_delete(request):
    cart = Cart(request)
    if (request.POST.get('action') == 'post'):
        # get stuff
        product_id = int(request.POST.get('product_id'))
        cart.delete(product_id)
        respose = JsonResponse({}, status=204)
        messages.success(request, message="Item is removed from cart... ")
        return respose
    return
