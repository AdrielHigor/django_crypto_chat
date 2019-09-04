from django.shortcuts import render, redirect
from app.core import forms, models
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

class UserSignUpView(CreateView):
    template_name = 'core/user/register.html'
    model = models.User
    form_class = forms.RegistrationForm
    success_url = "login"