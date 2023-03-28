# Generated by Django 4.1.6 on 2023-03-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('mobileNumber', models.CharField(default='', max_length=255)),
                ('profilePhoto', models.FileField(blank=True, default=None, upload_to='images')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
