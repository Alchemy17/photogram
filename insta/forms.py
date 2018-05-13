from django import forms
from .models import Image, Profile


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'likes', 'post_date']

class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'likes', 'post_date']
