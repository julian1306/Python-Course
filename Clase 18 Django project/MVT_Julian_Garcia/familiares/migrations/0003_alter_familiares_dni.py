# Generated by Django 4.0.4 on 2022-05-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_remove_familiares_fecha_alter_familiares_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.FloatField(max_length=8),
        ),
    ]
