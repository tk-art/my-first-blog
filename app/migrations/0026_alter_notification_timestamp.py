# Generated by Django 3.2.20 on 2023-08-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
