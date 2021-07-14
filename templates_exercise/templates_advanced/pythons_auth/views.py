from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from templates_advanced.pythons_auth.forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm()
        }
    return render(request, 'auth/register.html', context)

def login_view(request):
    username = 'admin'
    password = 'admin'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        redirect('index')
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
