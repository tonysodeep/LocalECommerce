class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_session_key')
        if 'cart_session_key' not in request.session:
            cart = self.session['cart_session_key'] = {}
        self.cart = cart
