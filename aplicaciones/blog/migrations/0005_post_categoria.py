# Generated by Django 4.0 on 2023-02-28 21:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='blog.categoria'),
            preserve_default=False,
        ),
    ]
