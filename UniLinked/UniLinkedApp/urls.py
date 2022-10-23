from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('login/', views.loginPage, name='login' ),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home')
]