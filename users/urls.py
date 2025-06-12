from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.public_profile_view, name='public_profile'),
]
