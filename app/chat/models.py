from django.db import models
from django.contrib.auth.models import User
from app.core import models as core


# Create your models here.
class Chat(core.CreateUpdateModel):
    users = models.ManyToManyField(core.User, related_name='chats', blank=True)

    class  Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

class Message(core.CreateUpdateModel):
    author = models.ForeignKey(core.User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='autor', related_name='author')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False, verbose_name='chat', related_name='chat')
    content = models.TextField(verbose_name='Mensagem')
    read = models.BooleanField(verbose_name="Read", default=False)

    class  Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    
    
