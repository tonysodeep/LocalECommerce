from store.models import Product
from decimal import Decimal


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_session_key')
        if 'cart_session_key' not in request.session:
            cart = self.session['cart_session_key'] = {}
        self.cart = cart

    def add(self, product: Product, quantity: int):
        product_id = str(product.id)
        product_qty = quantity
        if (product_id in self.cart):
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def update(self, product_id: int, product_qty: int):
        product_id = str(product_id)
        self.cart[product_id] = product_qty
        self.session.modified = True

    def delete(self, product_id: int):
        product_id = str(product_id)
        if product_id in self.cart:
            del (self.cart[product_id])

        self.session.modified = True

    def get_qty(self):
        return self.cart

    def cart_total(self) -> Decimal:
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        for key, value in self.cart.items():
            if products.get(pk=key).is_sale:
                total += Decimal(total) + \
                    products.get(pk=key).sale_price * value
            else:
                total += Decimal(total) + products.get(pk=key).price * value

        return total

    def __len__(self):
        return len(self.cart)
