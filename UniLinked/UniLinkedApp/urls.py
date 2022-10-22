from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('login/', views.login, name='login' ),
    path('register/', views.register, name='register')
]