# Generated by Django 5.0.1 on 2024-12-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_reserva_fecha_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='cod_lab',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
