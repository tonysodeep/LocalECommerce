from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_session_key')
        if 'cart_session_key' not in request.session:
            cart = self.session['cart_session_key'] = {}
        self.cart = cart

    def add(self, product: Product):
        product_id = str(product.id)
        if (product_id in self.cart):
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def __len__(self):
        return len(self.cart)
