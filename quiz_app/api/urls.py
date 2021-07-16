from django.urls import path
from .views import QuizView, QuestionView, AnswerView


urlpatterns = [
    path("quiz/", QuizView.as_view(), name="api-quiz"),
    path('question/', QuestionView.as_view(), name="api-question"),
    path('answer/', AnswerView.as_view(), name="api-answer"),
]