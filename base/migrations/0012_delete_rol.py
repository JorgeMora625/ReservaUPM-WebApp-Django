# Generated by Django 5.0.1 on 2024-04-27 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_alumnos_usuario_alter_profesores_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
