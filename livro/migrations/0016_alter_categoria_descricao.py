# Generated by Django 4.1.2 on 2022-11-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_livros_alugado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=60),
        ),
    ]