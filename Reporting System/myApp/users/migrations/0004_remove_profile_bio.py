# Generated by Django 5.1 on 2024-10-07 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
