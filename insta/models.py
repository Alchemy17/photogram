from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile/", blank=True)
    def __str__(self):
        return self.user.username
    @classmethod
    def get_profiles(cls):
        profiles = Profile.objects.all()
        return profiles
    
class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']