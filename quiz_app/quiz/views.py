from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuizForm
from .models import QuizModel, QuestionModel, AnswerModel


def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    questions = QuestionModel.objects.filter(quiz=1)
    answers = AnswerModel.objects.all()
    content = {
        'questions': questions,
        'answers': answers,
    }
    return render(request, 'quiz/quiz.html', content)