"""crypto_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from app.core import views as core
from app.chat import views as chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='core/user/login.html'), name='user-login'),
    path('user/login', auth_views.LoginView.as_view(template_name='core/user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/register', core.UserSignUpView.as_view(), name='user-register'),
    path('user/<str:pk>/profile/edit', core.UserProfileEditView.as_view(), name='user-edit-profile'),
    path('home/', chat.HomeView.as_view(), name='home-page'),
    path('home/chat/<str:pk>', chat.ChatView.as_view(), name='home-chat-page'),
    path('user/<str:pk>/profile', core.UserProfileView.as_view(), name='user-profile'),
    # path('chat/', chat.ChatView.as_view(), name='chat_page'),
    # path('create/', chat.MessageCreateView.as_view(), name='create'),
    # path('typing/', chat.MessageTypingView.as_view(), name='typing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
