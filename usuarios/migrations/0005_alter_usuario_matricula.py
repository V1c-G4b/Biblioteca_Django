# Generated by Django 4.1.2 on 2022-11-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_usuario_email_usuario_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(),
        )
    ]
