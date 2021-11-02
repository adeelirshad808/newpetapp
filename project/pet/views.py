from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pet/base.html')


def register(request):
    return render(request, 'pet/register.html')


def user_login(request):
    return render(request, 'pet/login.html')


def user_logout(request):
    return render(request, 'pet/logout.html')
