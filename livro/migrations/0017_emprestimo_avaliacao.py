# Generated by Django 4.1.2 on 2022-11-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_alter_categoria_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
