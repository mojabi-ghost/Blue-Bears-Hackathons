from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Account, Register
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from . auth import MyAuthBackEnd


# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password = password)
        #print(user)
        #print(username, password)
        if user is not None:
            print('Test')
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
        confirm = request.POST['confirm']
        university = request.POST['university']
        major = request.POST['major']
        
        myuser = User.objects.create_user(username, email, password)
        myuser.university = university
        myuser.major = major
        myuser.save()
        return redirect('login')
        

    return render(request, 'UniLinkedApp/register.html')

def home(request):
    return render(request, 'UniLinkedApp/connect.html')