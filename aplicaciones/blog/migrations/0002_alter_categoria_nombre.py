# Generated by Django 4.0 on 2023-02-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]