
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('details/<str:slug>', views.details, name='details'),
    path('jwellery/<str:slug>', views.jwellery, name='jwellery'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('products', views.products, name='products'),
]
