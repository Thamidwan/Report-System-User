# Generated by Django 5.1 on 2024-10-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_maintenancerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='maintenancerequest',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='maintenancerequest',
            name='unit_number',
            field=models.CharField(max_length=100),
        ),
    ]
