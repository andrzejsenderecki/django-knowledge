from django.shortcuts import render, redirect
from .forms import Register, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
    else:
        register_form = Register()
    return render(request, 'accounts/register.html', {'register_form': register_form})

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_data = login_form.cleaned_data
            user = authenticate(username=user_data['username'],
                                password=user_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'accounts/dashboard.html')
            else:
                return HttpResponse('Bad login data')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

