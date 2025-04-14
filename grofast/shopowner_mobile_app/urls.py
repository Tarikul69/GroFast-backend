from django.contrib import admin
from django.urls import include, path

from shopowner_mobile_app import views
from .views import api

urlpatterns = [
    path('api/', views.api, name='api'),
]