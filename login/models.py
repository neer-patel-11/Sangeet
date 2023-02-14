from django.db import models
from song.models import Playlist


class Person(models.Model):
   name = models.CharField(max_length=255)
   email= models.EmailField(max_length=255)
   mobileNumber =models.IntegerField()
   dob = models.DateField()
   profilePhoto = models.FileField(upload_to='images', default=None)
   username = models.CharField(max_length=255, unique=True , blank=False)
   password = models.CharField(max_length=25, blank=False)


   class Meta:
       abstract = True


class User(Person):
   playlists = models.ManyToManyField(Playlist, blank=True)


# Create your models here.
