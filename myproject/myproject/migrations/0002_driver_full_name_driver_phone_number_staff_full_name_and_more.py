# Generated by Django 5.1.5 on 2025-01-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='staff',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='admin',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
