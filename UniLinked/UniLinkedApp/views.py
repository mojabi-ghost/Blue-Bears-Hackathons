from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . models import Register
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password = password)
        print(user)
        if user is not None:
            login(request, username)
            return redirect('home')
        
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    context = {}
    return render(request, 'UniLinkedApp/login.html', context)

def register(request):
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        # print(request.POST)
        #print(form)
        if form.is_valid():
            # print('VALIDS')
            form.save()
            return HttpResponseRedirect(redirect_to=('/login/'))
        
    else:
        form = RegisterForm()
    return render(request, 'UniLinkedApp/register.html', {'form': form})

def home(request):
    return render(request, 'UniLinkedApp/connect.html')