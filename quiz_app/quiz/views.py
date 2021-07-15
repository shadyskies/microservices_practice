from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnswerForm
from .models import QuizModel, QuestionModel, AnswerModel
import time


def home(request):
    return render(request, 'quiz/home.html')


def quiz(request):
    questions = QuestionModel.objects.filter(quiz=1)
    answers = AnswerModel.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions, "answers": answers})


def score(request):
    print(request.POST)
    score = 0
    for i in request.POST:
        if i != 'csrfmiddlewaretoken':
            question_obj = QuestionModel.objects.get(title=i)
            print(f"corr: {question_obj.final_ans}, selected: {request.POST[i]}")
            if question_obj.final_ans == request.POST[i]:
                score += 1
    
    return render(request, 'quiz/score.html', {"score": score})
