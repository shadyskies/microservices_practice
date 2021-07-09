from django.urls import path
from .views import home, file_upload

urlpatterns = [
    path('ftp/', home, name='home'),
    path('file/', file_upload, name='file'),
]