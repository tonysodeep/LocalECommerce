from .store import Store


def store(request):
    return {'store': Store(request), }
