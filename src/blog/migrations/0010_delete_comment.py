# Generated by Django 4.2.1 on 2023-05-14 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
