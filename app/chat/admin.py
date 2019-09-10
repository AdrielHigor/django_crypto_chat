from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import Message, PrivateChat

admin.site.register(Message)
admin.site.register(PrivateChat)