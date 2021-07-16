from django.urls import path
from .views import create_quiz_view, create_question_view


urlpatterns = [
    path('create_quiz/', create_quiz_view, name='create-quiz'),
    path('create_question/', create_question_view, name='create-question'),
]