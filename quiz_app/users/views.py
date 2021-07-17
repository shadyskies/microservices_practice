import re
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from quiz.models import QuizModel, ResultModel
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('login')
    form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def base(request):
    return render(request,'users/base.html')

@login_required
def user_quizzes(request):
    user_quizzes = QuizModel.objects.filter(user=request.user) 
    user_results = ResultModel.objects.filter(user=request.user)
    quiz_completed_ids = [i.quiz.id for i in user_results]
    upcoming_quiz = [i for i in user_quizzes if i.id not in quiz_completed_ids]
    
    context = {
        'user_quizzes': user_quizzes, 
        'user_res': user_results,
        'upcoming_quiz': upcoming_quiz
    }
    return render(request, 'users/user-quiz.html', context)

@login_required
def user_results(request):
    user_results = ResultModel.objects.filter(user=request.user)
    context = {'user_res': user_results}
    return render(request, 'users/user-results.html', context)