"""Определяет схемы URL для pizza_logs."""
from django.urls import path
from . import views
app_name = 'pizza_logs'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
]