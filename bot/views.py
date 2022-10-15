import profile
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from instabot import Bot
from .models import InstagramAccounts
from django.http import HttpResponse
from . import forms

# Create your views here.
from os import remove
#remove("/config/eddyejembi_uuid_and_cookie.json")

instagram = Bot()

instagram_user = " "
instagram_post_link = " "
instagram_comment = " "
instagram_post = instagram.get_media_id_from_link(instagram_post_link)

"""def instagram(request):
    
    
    

    #profiles = InstagramAccounts.objects.values()

    profiles = InstagramAccounts.objects.values_list('username', 'password')
    d = []
    #return render(request, '/', {profiles})
    x = 0
    while x < len(profiles):
        d.append([profiles[x][0]])
        d.append([profiles[x][1]])
        instagram.login(username=profiles[x][0], password=profiles[x][0])
        instagram.follow(instagram_user) #follow user
        instagram.like(instagram_post) #like post
        instagram.comment(instagram_post, instagram_comment[0])
        print(d)
        x += 1
    return HttpResponse(d[1][0])"""

def get_profiles(request):
    form = forms.Client()

    if request.method == 'POST':
        form = forms.Client(request.POST)

        if form.is_valid():
            instagram_user = form.cleaned_data['profile_name']
            instagram_post_link = form.cleaned_data['post_link']
            instagram_comment = form.cleaned_data['comment']
        
        instagram_post = instagram.get_media_id_from_link(instagram_post_link)

        profiles = InstagramAccounts.objects.values_list('username', 'password')
        #d = []
        x = 0
        while x < len(profiles):
            #d.append([profiles[x][0]])
            #d.append([profiles[x][1]])
            try:
                instagram.login(username=profiles[x][0], password=profiles[x][0])
            except:
                print("An error occured trying to log in " + profiles[x][0])
            print(profiles[x][0])
            if instagram_user:
                instagram.follow(instagram_user) #follow user
                print("USER: " + instagram_user)
            if instagram_post_link:
                instagram.like(instagram_post) #like post
                print("POST LINK: " + instagram_post_link)
            if instagram_comment:
                instagram.comment(instagram_post, instagram_comment)
                print("COMMENT: " + instagram_comment)
            #print(d)
            x += 1

    return render(request, 'index.html', {'form':form})
    