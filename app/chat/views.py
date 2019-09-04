from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class HomeView(TemplateView):
    template_name = "chat/chat.html"