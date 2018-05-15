from django import forms
from .models import Image, Profile, Comment


class ImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','post_date', 'creator', 'likes', 'users_liked']

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
        widgets = {
            'comment_content': forms.TextInput(attrs={
                'class': u'comments-input form-control', 'placeholder': u'Insert Comment'})
        } 