from django.urls import path
from .views import QuizView, QuestionView


urlpatterns = [
    path("quiz/", QuizView.as_view(), name="api-quiz"),
    path('question/', QuestionView.as_view(), name="api-question"),
]