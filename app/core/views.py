from django.shortcuts import render, redirect, get_object_or_404
from app.core import forms, models
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse


class UserSignUpView(CreateView):
    template_name = 'core/user/register.html'
    model = models.User
    form_class = forms.RegistrationForm
    success_url = "login"

class UserProfileEditView(UpdateView):
    model = models.User
    template_name = 'core/user/profile/settings.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('home-page')

