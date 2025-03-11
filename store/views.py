from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .form import SignUpForm, UpdateUserForm


def home(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list, }
    return render(request, 'store/index.html', context)


def category_summary(request):
    return render(request, 'store/category_summary.html', {})


def about(request):
    return render(request, 'store/about.html', {})


def login_user(request):
    # check casesensitive
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


def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if (form.is_valid):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, message="you have success create user")
            return redirect('home')
        else:
            messages.success(request, "there a problem!. Please try agian")
            return redirect('register')

    return render(request, 'store/register.html', {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, message="you have success update user")
            return redirect('home')
        else:
            return render(request, 'store/update_user.html', {'user_form': user_form})
    else:
        messages.success(request, message="you must login to access this page")
        return redirect('login')


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product.html', {'product': product})


def category(request, foo):
    try:
        category = Category.objects.get(name=foo)
        categories = Category.objects.all()
        products = Product.objects.filter(category=category)
        context = {
            'product_list': products,
            'category': category
        }
        return render(request, 'store/category.html', context)
    except Exception as e:
        print(e)
        messages.success(request, 'the category does not exist')
        return redirect('home')
