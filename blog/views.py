from django.shortcuts import render

posts = [
    {
        'author': 'George',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 18'
    },
    {
        'author': 'John',
        'title': 'Blog post 2',
        'content': 'First second content',
        'date_posted': 'August 27, 18'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html') 