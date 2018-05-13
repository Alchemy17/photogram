from django import forms
from .models import Image, Profile


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','post_date']

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []