# Generated by Django 4.0.4 on 2022-05-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nanme', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('SKU', models.CharField(max_length=30, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]