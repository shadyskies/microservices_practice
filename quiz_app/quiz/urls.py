from django.urls import path
from .views import home
from .views import quiz


urlpatterns = [
    path('', home, name='home'),
    path('quiz/', quiz, name='quiz'),
]