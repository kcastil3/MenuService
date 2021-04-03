from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from signup.forms import LogInForm, CustomUserCreationForm, CreateNewUserForm
from django.template import RequestContext
from .managers import UserManager
from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            form.clean()
            email = request.POST['email']
            password_1 = request.POST['password_1']
            password_2 = request.POST['password_2']
            if password_1 == password_2:
                user = get_user_model().objects.create_user(email=email, password=password_1) # Create and login new user
                user = authenticate(request, username=email, password=password_1)
            if user is not None:
                login(request, user)
        return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            form.clean()
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
        return render(request, 'index.html')
   

def logout_view(request):
    logout(request)
    return redirect('/')
