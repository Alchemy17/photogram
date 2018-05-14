from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile/", blank=True)
    def __str__(self):
        return self.user.username
    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(user__username__icontains=query).first()   
        return result

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.caption
    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    @classmethod
    def get_Image_by_profile(cls,profile):
        images = cls.objects.filter(profile=profile).all()
        return images

    class Meta:
        ordering = ['-post_date']

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment_content = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_post_comments(cls,post_id):

        post_comments = Comment.objects.filter(post=post_id)

        return post_comments