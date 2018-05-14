from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponse, HttpResponseRedirect
from .models import Image, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ImagePost, EditProfile
from django.contrib.auth.models import User


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

        form = ImagePost(request.POST, request.FILES)

        if form.is_valid:
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
            return redirect('profiles', current_user.username)
    else:
        form = ImagePost()
    
    title = "New Post"
    content = {
        "form":form,
        "title":title
    }
    return render(request,'post.html', content)


@login_required(login_url='/accounts/login/')
def profiles(request, profile_id):

    current_user = request.user


    profiles = Image.objects.filter(creator__username__iexact=profile_id)
    print(profiles)
    profile = Profile.objects.get(user__username__exact=profile_id)
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


def explore(request):
    profiles = Profile.get_all()
    content = {
        "profiles":profiles,
    }
    return render(request,"explore.html", content)

@login_required(login_url='/accounts/register')
def edit(request):
    
    profile= request.user.profile

    if request.method == 'POST':

        form = EditProfile(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            current_user = request.user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profiles', current_user.username)
    else:
        form = EditProfile()
    
    title = "New Post"
    content = {
        "form":form,
        "title":title
    }
    return render(request,'editProfile.html', content)

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_images = Profile.searched(search_term)
        images= Image.get_Image_by_profile(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
@login_required(login_url='/accounts/register')
def like(request):

     if request.GET.has_key('id'):
        try:
            id = request.GET['id']
            post = Image.objects.get(id=id)
            user_liked = post.users_liked.filter(username=request.user.username)
            if not user_liked:
                post.likes += 1
                post.users_liked.add(request.user)
                post.save()
        except ObjectDoesNotExist:
            raise Http404('Post not found.')
        
     if request.META.has_key('HTTP_REFERER'):
         return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
     return HttpResponseRedirect('/')