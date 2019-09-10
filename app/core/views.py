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

    #Prevent user changing URL <pk> to edit others profiles data
    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.pk == request.user.pk
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('/user/login')
        return super(UserProfileEditView, self).dispatch(
            request, *args, **kwargs)