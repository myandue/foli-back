from django.shortcuts import render, redirect
from .forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("login")  # 회원가입 후 로그인 페이지로 리디렉션
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
