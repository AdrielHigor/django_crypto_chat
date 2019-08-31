from django.db import models
from django.contrib.auth.models import User
from app.core import models as core


# Create your models here.

class Message(core.CreateUpdateModel):
    author= models.ForeignKey(core.User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='autor', related_name='author')
    content= models.TextField(verbose_name='Mensagem')

    class  Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
    
class PrivateChat(core.CreateUpdateModel):
    msgprivadas= models.TextField(verbose_name='Mensagem')
    usersecret= models.ForeignKey(core.User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Nome', related_name='idsecret')

    class  Meta:
        verbose_name = 'Chat Privado'
        verbose_name_plural = 'Chats Privados'
    
