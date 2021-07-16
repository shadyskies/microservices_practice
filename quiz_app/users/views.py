import re
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from quiz.models import QuizModel, ResultModel


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


def dashboard(request):
    user_results = ResultModel.objects.filter(user=request.user)
    user_quizes = QuizModel.objects.filter(user=request.user) 

    context = {
        'user_res': user_results,
        'user_quizes': user_quizes
    }
    return render(request,'users/dashboard.html', context=context)