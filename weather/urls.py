# weather/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('weather/', views.get_weather, name='get_weather'),  # Weather data route
]
