from django.contrib import admin
from song.models import Song, Podcast, Comment

admin.site.register(Song)
admin.site.register(Podcast)
# admin.site.register(Playlist)
admin.site.register(Comment)

# Register your models here.
