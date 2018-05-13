from django import forms
from .models import Image, Comment


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'post_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post']
