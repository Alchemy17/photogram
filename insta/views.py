from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponse
from .models import Image, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewsPostForm, NewCommentForm


# Create your views here.

@login_required(login_url='/accounts/register')
def welcome(request):

    current_user = request.user

    images = Image.objects.all()
    profiles = Profile.objects.all()
    content = {
        "images": images,
        "profiles": profiles,
        "user": current_user
    }
    

    return render(request, 'index.html', content)

@login_required(login_url='/accounts/register')
def post(request):
    current_user = request.user
    profile= request.user.profile
    if request.method == 'POST':

        form = NewsPostForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.profile = profile
            post.save()

            return redirect('profiles', current_user.username)

    else:

        form = NewsPostForm()
    
    title = "New Post"
    content = {
        "form":form,
        "title":title
    }
    return render(request,'post.html', content)


@login_required(login_url='/accounts/login/')
def profiles(request, profile_id):

    current_user = request.user


    profiles = Image.objects.filter(creator__username__exact=profile_id)
    profile = Profile.objects.get(user__username__exact=profiles[0].creator.username)
    content = {
        "profiles":profiles,
        "profile":profile,
        "user": current_user,
        "profile_id": profile_id
    }
    return render(request,"profile.html", content)


@login_required(login_url='/accounts/login/')
def image(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})