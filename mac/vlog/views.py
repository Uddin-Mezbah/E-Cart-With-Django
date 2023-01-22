from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'vlog/index.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    #print(post)
    return render(request, 'vlog/blogpost.html',
                  {'post':post})
