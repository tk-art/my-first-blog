# Generated by Django 3.2.19 on 2023-07-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_profile_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.CharField(default='宮崎県宮崎市⚪︎⚪︎⚪︎⚪︎⚪︎', max_length=100),
            preserve_default=False,
        ),
    ]
