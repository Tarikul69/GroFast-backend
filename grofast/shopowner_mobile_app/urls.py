from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('api/', views.api, name='api'),
    path('product_category/', views.category_list, name='product_category'),
    path('category_list_byid/<int:shop_id>/', views.category_list_id, name='category_list_byid'),
]