from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/<int:product_id>/', views.product, name='product_detail'),
    path('category/<str:foo>/', views.category, name='category'),
    path('category_summary', views.category_summary, name='category_summary')
]
