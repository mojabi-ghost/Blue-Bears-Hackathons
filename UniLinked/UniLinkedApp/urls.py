from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('login/', views.loginPage, name='login' ),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.connect, name='connect'),
    path('profile/', views.profile, name='users-profile'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]