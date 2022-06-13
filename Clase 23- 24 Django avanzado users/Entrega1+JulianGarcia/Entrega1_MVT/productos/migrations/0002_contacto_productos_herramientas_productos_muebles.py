# Generated by Django 4.0.4 on 2022-06-08 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos_herramientas',
            fields=[
                ('productos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='productos.productos')),
                ('energia', models.CharField(max_length=30)),
                ('clase', models.CharField(max_length=30)),
            ],
            bases=('productos.productos',),
        ),
        migrations.CreateModel(
            name='Productos_muebles',
            fields=[
                ('productos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='productos.productos')),
                ('tipo', models.CharField(max_length=30)),
                ('capacidad', models.CharField(max_length=30)),
            ],
            bases=('productos.productos',),
        ),
    ]