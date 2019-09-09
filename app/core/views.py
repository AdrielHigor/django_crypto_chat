from django.shortcuts import render, redirect
from app.core import forms, models
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
# Create your views here.


class UserSignUpView(CreateView):
    template_name = 'core/user/register.html'
    model = models.User
    form_class = forms.RegistrationForm
    success_url = "login"


class UserProfileEditView(UpdateView):
    template_name = 'core/user/profile/settings.html'
    model = models.User
    form_class = forms.UserProfileEditForm

    def post(self, request, *args, **kwargs):
        print(request)
        return super().post(request, *args, **kwargs)