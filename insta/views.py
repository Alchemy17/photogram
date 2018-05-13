from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Profile

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    content = {
        "images": images,
        "profiles": profiles
    }

    return render(request, 'index.html', content)

def profiles(request, profile_id):

    profiles = Image.objects.filter(creator__username__exact=profile_id)

    return render(request,"profile.html", {"profiles":profiles})