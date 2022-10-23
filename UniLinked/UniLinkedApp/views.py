from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Account, Register
from . forms import AccountAuthenticationForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from . auth import MyAuthBackEnd


# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        # form = AccountAuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user:
            login(request, user)
            return redirect('home')
        
        else:
            print('Not work')
            messages.info(request, 'Username or Password is incorrect')
        
    context = {}
    return render(request, 'UniLinkedApp/login.html', context)

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        university = request.POST['university']
        major = request.POST['major']
        
        myuser = Account.objects.create_user(username, password)
        myuser.email = email
        myuser.university = university
        myuser.major = major
        myuser.save()
        return redirect('login')
        

    return render(request, 'UniLinkedApp/register.html')

def home(request):
    return render(request, 'UniLinkedApp/connect.html')