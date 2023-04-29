from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


posts = [
    {
        'author': 'NGeorge',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Febuary 18, 2023'
    },
    {
        'author': 'JGeorge',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Febuary 18, 2023'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    
    return render(request,'blog/about.html', )

def contact(request):
    
    return render(request,'blog/contact.html', )