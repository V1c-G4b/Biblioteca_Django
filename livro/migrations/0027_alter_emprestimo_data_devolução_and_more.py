# Generated by Django 4.1.2 on 2022-11-27 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0026_livros_img_alter_emprestimo_data_devolução_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolução',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 0, 12, 19, 311592)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 27, 0, 12, 19, 311639)),
        ),
        migrations.AlterField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='foto_livro'),
        ),
    ]
