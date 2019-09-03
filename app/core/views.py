from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'core/user/login.html', {})

def registration(request):
    return render(request, 'core/user/register.html', {})
    