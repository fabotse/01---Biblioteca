# Generated by Django 4.1.2 on 2022-10-06 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_ativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ativo',
        ),
    ]
