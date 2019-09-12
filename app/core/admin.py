from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth

from .models import User, Friendship

admin.site.register(User)
admin.site.register(Friendship)

# Register your models here.
