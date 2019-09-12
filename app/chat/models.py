from django.db import models
from django.contrib.auth.models import User
from app.core import models as core
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Chat(core.CreateUpdateModel):
    chat_name = models.CharField(max_length=150, blank=True, verbose_name='chat_name') 
    users = models.ManyToManyField(core.User, blank=False, verbose_name='users')
    picture = models.ImageField(null=False, blank=True, verbose_name='picture', upload_to='chat/chat_img/', default='chat/chat_img/default.png')
    picture_thumb = ImageSpecField(source='picture', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})
    creator = models.ForeignKey(core.User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='creator', related_name='creator')

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

    
    
