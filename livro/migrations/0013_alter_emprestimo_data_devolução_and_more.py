# Generated by Django 4.1.2 on 2022-11-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimo_nome_alugado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolução',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
