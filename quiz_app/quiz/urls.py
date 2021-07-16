from django.urls import path
from .views import home, quiz, score


urlpatterns = [
    path('', home, name='home'),
    path('quiz/<int:pk>', quiz, name='quiz'),
    path('score/<int:pk>', score, name='score'),
]