from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    
    class Meta:
        model=Song
        fields="__all__"
        
