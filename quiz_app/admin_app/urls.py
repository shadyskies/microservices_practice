from django.urls import path
from .views import create_quiz_view, create_question_view, create_answer_view


urlpatterns = [
    path('create_quiz/', create_quiz_view, name='create-quiz'),
    path('create_question/', create_question_view, name='create-question'),
    path('create_answer/', create_answer_view, name='create-answer'),

]