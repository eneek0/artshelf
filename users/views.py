from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from users.forms import UserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('main:index') 
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    context = {
    }
    return render(request, 'users/', context)