# Generated by Django 2.2.4 on 2019-08-31 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190831_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_seen',
        ),
    ]