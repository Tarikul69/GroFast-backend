from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('shops/', views.shop_list, name='shop_list'),
    path('login_api/', views.login_user,),
    path('registration_api/', views.register_user, ),
    path('category_list_id/<int:shop_id>/', views.category_list_id, name='category_list_id'),

]