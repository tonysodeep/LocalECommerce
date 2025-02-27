from .models import Category


class Store():
    def __init__(self, request):
        category_list = Category.objects.all()
        self.category_list = category_list
