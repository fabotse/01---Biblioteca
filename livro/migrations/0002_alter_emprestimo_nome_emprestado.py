# Generated by Django 4.1.2 on 2022-10-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.CharField(max_length=200),
        ),
    ]
