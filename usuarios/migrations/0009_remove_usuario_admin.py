# Generated by Django 4.1.2 on 2022-11-17 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_usuario_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='admin',
        ),
    ]
