from django.shortcuts import render

posts = [
    {
        'author': 'Joshua Brandon',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 21, 2019'
    },
    {
        'author': 'Joshua Brandon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 22, 2019'
    }
]

# Create your views here
def home(request):
    context = {
        # 'posts' will be available in the template listed below
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # 'title' is the context for this view
    return render(request, 'blog/about.html', {'title': 'About'})