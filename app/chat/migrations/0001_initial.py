# Generated by Django 2.2.3 on 2019-08-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Nome')),
                ('idPrivado', models.CharField(max_length=30, verbose_name='ID privado')),
                ('idPublico', models.CharField(max_length=30, verbose_name='ID publico')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
        ),
    ]
