# Generated by Django 5.1.2 on 2024-11-01 12:47

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_DRF', '0002_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Enter your contat number')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
