# Generated by Django 4.1.2 on 2022-11-09 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_emprestimo_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 10, 58, 7, 448830)),
        ),
    ]
