from django.shortcuts import redirect, render
from .forms import UserRegisterForm


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