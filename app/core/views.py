from django.shortcuts import render, redirect, get_object_or_404
from app.core import forms, models
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse


class UserSignUpView(CreateView):
    template_name = 'core/user/register.html'
    model = models.User
    form_class = forms.RegistrationForm
    success_url = "login"

    def get(self, request, *args, **kwargs):
        self.object = None
        return super(UserSignUpView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        print(request.POST)
        return super(UserSignUpView, self).post(request, *args, **kwargs)


class UserProfileEditView(UpdateView):
    model = models.User
    template_name = 'core/user/profile/settings.html'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        # if you are passing 'pk' from 'urls' to 'DeleteView' for company
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        user_id=self.kwargs['pk']
        return reverse_lazy('user-profile', kwargs={'pk': user_id})

    
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

class UserProfileView(UpdateView):
    model = models.User
    template_name = 'core/user/profile/profile.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('home-page')