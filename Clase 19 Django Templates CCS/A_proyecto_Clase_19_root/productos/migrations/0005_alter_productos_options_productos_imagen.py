# Generated by Django 4.0.4 on 2022-06-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_procutos_productos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos_imagenes'),
        ),
    ]
