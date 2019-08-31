from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class usuario(models.Model):

    username = models.CharField(max_length=100, verbose_name='Nome')
    idPrivado = models.CharField(max_length=30, verbose_name='ID privado')
    idPublico = models.CharField(max_length=30, verbose_name='ID publico')
    senha = models.CharField(max_length=255, verbose_name='Senha')
    email = models.CharField(max_length=255, verbose_name='Email')

    def __str__(self):
        return self.username

    class Meta:
        unique_together = (('idPrivado', 'idPublico', 'email'),)
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios' 