# Generated by Django 4.1.7 on 2023-03-28 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_remove_podcast_size_remove_song_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='comments',
        ),
    ]
