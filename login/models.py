from django.db import models
# from song.models import Playlist
# from django.contrib.auth.models import User 


class Person(models.Model):
   name = models.CharField(max_length=255, default='')
   email= models.EmailField(max_length=255, default='')
   mobileNumber =models.CharField(max_length=255, default='')
   profilePhoto = models.FileField(upload_to='images',default=None, blank=True)
   username = models.CharField(max_length=255, unique=True , blank=False)
   password = models.CharField(max_length=25, blank=False)


   class Meta:
       abstract = True


class Users(Person):
   # playlists = models.ManyToManyField(Playlist, blank=True)
      
   def __str__(self):
      return self.name



