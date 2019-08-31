from django.db import models
from django.contrib.auth.models import User
from app.core import models as core



# Create your models here.

class chatPublico(models.Model):
    msgpublica= models.TextField(verbose_name='Mensagens')
    userpublic= models.ForeignKey(core.usuario, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Nome', related_name='idsocial')

    class  Meta:
        verbose_name = 'Chat Publico'
        verbose_name_plural = 'Chats Publicos'
    
class chatPrivado(models.Model):
    msgprivadas= models.TextField(verbose_name='Mensagens')
    usersecret= models.ForeignKey(core.usuario, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Nome', related_name='idsecret')

    class  Meta:
        verbose_name = 'Chat Privado'
        verbose_name_plural = 'Chats Privados'
    
