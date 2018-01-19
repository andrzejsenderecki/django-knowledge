from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
    else:
        register_form = Register()

    return render(request, 'accounts/register.html', {'register_form': register_form})
