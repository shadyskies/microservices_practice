from django.urls import path
from .views import home

urlpatterns = [
    path('ftp/', home, name='home'),
]