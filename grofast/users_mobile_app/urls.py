from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('shops/', views.shop_list, name='shop_list'),
    path('login_api/', views.admin_index, name='admin_index'),
    path('registration_api/', views.registration, name='registration'),
]