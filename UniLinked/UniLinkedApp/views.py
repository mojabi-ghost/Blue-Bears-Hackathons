from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Account, Register, Room, Message
from . forms import AccountAuthenticationForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from . auth import MyAuthBackEnd
from django.contrib.auth.decorators import login_required

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

def about(request):
    return render(request, 'UniLinkedApp/about.html')

def contact(request):
    return render(request, 'UniLinkedApp/contact.html')

def home(request):
    return render(request, 'UniLinkedApp/home.html')

def connect(request):
    return render(request, 'UniLinkedApp/connect.html')

@login_required
def profile(request):
    return render(request, 'UniLinkedApp/profile.html')

@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'UniLinkedApp/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

@login_required
def checkview(request):
    print('Test')
    room = request.POST['room_name']
    username = request.POST['username']
    print(room, username)
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        print('Created')
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})