# Generated by Django 4.1.6 on 2023-03-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('mobileNumber', models.CharField(default='', max_length=255)),
                ('dob', models.DateField(blank=True, default='')),
                ('profilePhoto', models.FileField(default=None, upload_to='')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('playlists', models.ManyToManyField(blank=True, to='song.playlist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
