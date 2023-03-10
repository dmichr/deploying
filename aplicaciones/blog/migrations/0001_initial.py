# Generated by Django 4.0 on 2023-02-24 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres de Autor')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos de Autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('correo', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activo/Autor no Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de cracion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombres')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoría Activada/Categoría no  Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de cracion')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
    ]
