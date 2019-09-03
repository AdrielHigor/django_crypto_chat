from django.shortcuts import render, redirect
from app.core import forms, models
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

# def login(request):
#     return render(request, 'core/user/login.html', {})

# def registration(request):
#     if request.method == "POST":
#         form = core.RegistrationForm(request.POST)
#         if form.is_valid():          
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             # login(request, user)
#             return redirect("main:homepage")

#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request = request,
#                           template_name = "core/user/register.html",
#                           context={"form":form})
#     else:
#         form = core.RegistrationForm
#         return render(request = request,
#                     template_name = "core/user/register.html",
#                     context={"form":form})

class UserSignUpView(CreateView):
    template_name = 'core/user/register.html'
    model = models.User
    form_class = forms.RegistrationForm
