from django import forms
from .models import Image


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'likes', 'post_date']
