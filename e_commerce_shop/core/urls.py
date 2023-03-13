from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('product/<slug:slug>', views.product_info, name="product-info")
]
