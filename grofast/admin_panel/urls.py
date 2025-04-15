from django.contrib import admin
from django.urls import include, path

from admin_panel import views
from .views import registration

urlpatterns = [
    path('registration/', views.registration, name='registration'),
]