# Generated by Django 5.1.5 on 2025-01-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_driver_full_name_driver_phone_number_staff_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='job_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
