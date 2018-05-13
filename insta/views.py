from django.shortcuts import render
from django.http  import HttpResponse, Http404, HttpResponse
from .models import Image, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    content = {
        "images": images,
        "profiles": profiles
    }

    return render(request, 'index.html', content)

@login_required(login_url='/accounts/login/')
def profiles(request, profile_id):

    profiles = Image.objects.filter(creator__username__exact=profile_id)
    profile = Profile.objects.get(user__username__exact=profiles[0].creator.username)
    content = {
        "profiles":profiles,
        "profile":profile
    }
    return render(request,"profile.html", content)


@login_required(login_url='/accounts/login/')
def image(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})