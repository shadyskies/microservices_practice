from django.urls import path
from .views import home, quiz, score


urlpatterns = [
    path('', home, name='home'),
    path('quiz/', quiz, name='quiz'),
    path('score/', score, name='score'),
]