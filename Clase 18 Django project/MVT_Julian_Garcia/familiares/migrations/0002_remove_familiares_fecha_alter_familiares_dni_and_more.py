# Generated by Django 4.0.4 on 2022-05-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiares',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='familiares',
            name='dni',
            field=models.FloatField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='edad',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]
