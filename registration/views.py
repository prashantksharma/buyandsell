from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, UserTypeForm

# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

def login(request):
    return render(request, 'mysite/login.html')

def logout(request):
    return render(request, 'mysite/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'mysite/register.html', {'form' : form})

def choose_type(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            formObj = form.cleaned_data
            user_type = formObj['choice']
        else:
            form = UserTypeForm()
    return render(request, 'mysite/register.html', {'form': form} )
    # return HttpResponseRedirect("<h2>CHOOSE THE TYPE</h2>")