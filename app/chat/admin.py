from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import Message, Chat

admin.site.register(Message)
admin.site.register(Chat)