from django import forms
from .models import Image, Profile, Comment


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','post_date']

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post'] 