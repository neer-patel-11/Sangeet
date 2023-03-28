from django import forms
from .models import Song, Podcast

class SongForm(forms.ModelForm):
    
    class Meta:
        model=Song
        fields="__all__"
        
class PodcastForm(forms.ModelForm):
    
    class Meta:
        model=Podcast
        fields="__all__"