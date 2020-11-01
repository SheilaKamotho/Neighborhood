# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Business
from .forms import NewPostForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    profile=Profile.objects.all()
    posts=Post.objects.all()
    return render(request, 'home/home.html',{"profile":profile, "posts":posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')
        
    else:
        form = NewPostForm()
    return render(request, 'home/new_posts.html', {"form":form, "current_user":current_user})

@login_required(login_url='/accounts/login/')
def business(request):
    businesses=Business.objects.all()
    return render(request, 'home/business.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'home/about.html')

@login_required(login_url='/accounts/login/')
def contact(request):
    return render(request, 'home/contact.html')

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'home/search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'home/search.html',{"message":message})