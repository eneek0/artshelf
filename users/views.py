from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from users.forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse, reverse_lazy
from goods.models import Products 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()


    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    context = {
    }
    return redirect(reverse('main:index'))

# def profile_view(request):
#     user = request.user
#     user_products = Products.objects.filter(user=user)
#     return render(request, 'users/profile.html', {
#         'user_products': user_products
#     })

def profile_view(request):
    print('Текущий пользователь:', request.user.username)
    print('ID пользователя:', request.user.id)

    user_products = Products.objects.filter(user=request.user)
    print('Количество товаров:', user_products.count())

    # Избранные товары текущего пользователя
    favorite_products = Products.objects.filter(favorited_by__user=request.user)

    return render(request, 'users/profile.html', {
        'user_products': user_products,
        'favorite_products': favorite_products,
        'profile_user': request.user  # чтобы шаблон отображал текущего пользователя
    })

def public_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    user_products = Products.objects.filter(user=profile_user)
    return render(request, 'users/profile.html', {
        'profile_user': profile_user,
        'user_products': user_products
    })