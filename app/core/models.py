from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Permission
import uuid

class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    # idPrivado = models.CharField(max_length=30, verbose_name='ID privado')
    # idPublico = models.CharField(max_length=30, verbose_name='ID publico')
    last_seen = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    connection_status = models.BooleanField(null=False, blank=False, default=False)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
