from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('users/', views.users_list, name='users_list'),
    path('shop_registration/', views.shop_registration, name='shop_registration'),
    path('shop_list/', views.shop_list, name='shop_list'),

    #Admin Panel UI path
    path('admin_index/', views.admin_index, name='admin_index'),
]