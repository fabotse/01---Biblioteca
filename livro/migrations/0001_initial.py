# Generated by Django 4.1.2 on 2022-10-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.DateTimeField()),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_duracao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('co_autor', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('emprestado', models.BooleanField(default=False)),
            ],
        ),
    ]
