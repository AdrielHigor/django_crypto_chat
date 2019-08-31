from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import Message

admin.site.register(Message)