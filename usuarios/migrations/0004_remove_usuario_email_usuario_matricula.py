# Generated by Django 4.1.2 on 2022-11-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_matricula_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AddField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
