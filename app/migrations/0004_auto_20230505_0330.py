# Generated by Django 3.2.19 on 2023-05-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
