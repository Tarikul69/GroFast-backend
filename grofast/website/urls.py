from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from . import views

urlpatterns = [
    path('download_app/', views.download_app, name='download_app'),
]