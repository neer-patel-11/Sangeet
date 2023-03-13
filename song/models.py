from django.db import models




# Create your models here.
LANGUAGE_CHOICES = (
   ('english', 'English'),
   ('hindi', 'Hindi'),
   ('gujarati','Gujarati')
)


class Comment(models.Model):
   comments = models.CharField(max_length=500)


class Audio(models.Model):
   name = models.CharField(max_length=255)
   audioFile = models.FileField(blank=False)
   artist = models.CharField(max_length=255)
   duration = models.TimeField(auto_now_add=False, blank=False)
   thumbnail = models.FileField(upload_to='images', default=None)
   languages = models.CharField(max_length=max(len(v[0]) for v in LANGUAGE_CHOICES),choices=LANGUAGE_CHOICES, default='hindi')
   uploadDate = models.DateTimeField(auto_now_add=True)
   likeCount = models.IntegerField(default=0)
   # comment = ManyToManyField(models.CharField(max_length=500))
   size =models.FloatField()#MB


   class Meta:
       abstract = True


   def like(self):
       self.likeCount = self.likeCount + 1
   #comment and viewDetails remaining functions




TYPE_OF_SONG = (
   ('sad', 'Sad'),
   ('romantic', 'Romantic'),
   ('pop','Pop'),
   ('rap','Rap'),
   ('bhajan' ,'Bhajan'),
   ('rock','Rock'),
   ('other' , 'Other')
)


class Song(Audio):
   comments = models.ManyToManyField(Comment, blank=True)
   type = models.CharField(max_length=max(len(v[0]) for v in TYPE_OF_SONG),choices=TYPE_OF_SONG, default='bhajan')

   
   def __str__(self):
      return self.name


TYPE_OF_PODCAST = (
   ('scientific', 'Scientific'),
   ('geopolitics', 'Geopolitics'),
   ('humor','Humor'),
   ('religious','Religious'),
   ('buisness' ,'Buisness'),
   ('historical','Historical'),
   ('interview' , 'Interview')
)


class Podcast(Audio):
   comments = models.ManyToManyField(Comment, blank=True)
   type=models.CharField(max_length=max(len(v[0]) for v in TYPE_OF_PODCAST),choices=TYPE_OF_PODCAST)

   
   def __str__(self):
      return self.name




class Playlist(models.Model):
   name = models.CharField(max_length=255)
   totalSongs = models.IntegerField(default=0)
   songs = models.ManyToManyField(Song)

   
   def __str__(self):
      return self.name
