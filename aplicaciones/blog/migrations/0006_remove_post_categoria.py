# Generated by Django 4.0 on 2023-02-28 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
    ]