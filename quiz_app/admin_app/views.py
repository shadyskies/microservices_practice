from django.shortcuts import render, redirect
from .forms import CreateQuizForm, CreateQuestionForm
from quiz.models import QuizModel
from rest_framework.response import Response
from rest_framework import status
import requests

# creating quiz
def create_quiz_view(request):
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        print("--------------------")
        if form.is_valid():
            print('form is valid')
            data = form.cleaned_data
            form.save()
            return redirect(f'create-question')
    form = CreateQuizForm()
    context = {'form': form}
    return render(request, "admin_app/create-quiz.html" , context=context)

#creating questions
def create_question_view(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST, request.FILES)
        print("--------------------")
        if form.is_valid():
            print('form is valid')
            form.save()
        else:
            print(form.errors)
    form = CreateQuestionForm()
    return render(request, "admin_app/create-question.html" ,{"form": form})