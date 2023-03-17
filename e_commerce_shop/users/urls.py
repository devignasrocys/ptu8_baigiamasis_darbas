from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-orders/', views.track_orders, name='my-orders'),
    path('my-order/order-details/<int:pk>/', views.order_details, name='order-details'),
    path('profile-management/', views.profile_management, name='profile-management'),
    path('manage-shipping/', views.manage_shipping, name='manage-shipping'),
    path('delete-account/', views.delete_account, name='delete-account')
]
