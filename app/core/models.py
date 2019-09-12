from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Permission
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models import Q
import uuid


class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="uuiduser_set", related_query_name="user")
    picture = models.ImageField(
        null=False, blank=True, verbose_name='picture', upload_to='user/profile_picture/', default='user/profile_picture/default.png')
    picture_thumb = ImageSpecField(source='picture', processors=[
                                   ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})
    last_seen = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    connection_status = models.BooleanField(
        null=False, blank=False, default=False)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    def __str__(self):
        return self.username

    def get_friends(self):
        user = self
        return Friendship.objects.filter(Q(creator=user) | Q(friend=user))

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Friendship(CreateUpdateModel):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_creator_set")
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friend_set")

    class Meta:
        verbose_name = 'Amizade'
        verbose_name_plural = 'Amizades'
