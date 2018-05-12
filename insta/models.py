from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile-pic/", blank=True)
    def __str__(self):
        return self.user.username
    @classmethod
    def get_profiles(cls):
        profiles = Profile.objects.all()
        return profiles