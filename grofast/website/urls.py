from django.urls import include, path
from website import views
from . import views



urlpatterns = [
    path('download_app/', views.download_app, name='download_app'),
]