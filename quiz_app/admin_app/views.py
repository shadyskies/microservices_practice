from django.shortcuts import render, redirect
from .forms import CreateQuizForm, CreateQuestionForm, CreateAnswerForm


def create_quiz_view(request):
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        print("--------------------")
        print(f"FORM: {form}")
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('create-question')
    form = CreateQuizForm()
    return render(request, "admin_app/create-quiz.html" ,{"form": form})

def create_question_view(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        print("--------------------")
        print(f"FORM: {form}")
        if form.is_valid():
            print('form is valid')
            form.save()
            if form.cleaned_data['question_type'] == 'text':
                return redirect('home')
            else:
                return redirect('create-answer')
        else:
            print(form.errors)
    form = CreateQuestionForm()
    return render(request, "admin_app/create-question.html" ,{"form": form})


def create_answer_view(request):
    if request.method == 'POST':
        form = CreateAnswerForm(request.POST)
        print("--------------------")
        print(f"FORM: {form}")
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    form = CreateAnswerForm()
    return render(request, "admin_app/create-options.html" ,{"form": form})
