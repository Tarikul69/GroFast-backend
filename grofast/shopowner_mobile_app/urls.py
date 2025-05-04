from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('api/', views.api, name='api'),
    path('product_category/', views.category_list, name='product_category'),
]