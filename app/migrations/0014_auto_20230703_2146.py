# Generated by Django 3.2.19 on 2023-07-03 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20230701_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='like',
        ),
    ]