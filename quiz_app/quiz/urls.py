from django.urls import path
from .views import quiz, score


urlpatterns = [
    path('<int:pk>/', quiz, name='quiz'),
    path('score/<int:pk>/', score, name='score'),
]