# Generated by Django 4.1.2 on 2022-11-01 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_livros_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='genêro',
        ),
    ]
