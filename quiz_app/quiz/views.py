from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AnswerForm
from .models import QuizModel, QuestionModel, AnswerModel, ResultModel
import datetime


def home(request):
    return render(request, 'quiz/home.html')


def quiz(request, pk):
    quiz = QuizModel.objects.get(id=pk)
    if ResultModel.objects.get(user=request.user, quiz=pk):
        return HttpResponse("<h3>Already attempted</h3>")
    questions = QuestionModel.objects.filter(quiz=pk)
    answers = AnswerModel.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions, "answers": answers})


#calculate scores for quiz, create result obj
def score(request, pk):
    print(request.POST)
    score = 0
    for i in request.POST:
        if i != 'csrfmiddlewaretoken':
            question_obj = QuestionModel.objects.get(title=i)
            print(f"corr: {question_obj.final_ans}, selected: {request.POST[i]}")
            if question_obj.final_ans == request.POST[i]:
                score += 1
    quiz = QuizModel.objects.get(id=pk)
    score_obj = ResultModel.objects.create(user=request.user, score=score, date=datetime.date.today(), quiz=quiz)   
    return render(request, 'quiz/score.html', {"score": score})
