# Generated by Django 4.1.6 on 2023-03-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='dob',
        ),
    ]
