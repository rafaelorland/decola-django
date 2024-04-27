from django.shortcuts import get_object_or_404, render, HttpResponse
from blog.models import Post

def blog(request, id=None):
    if id is not None:
    
        return blog_detail(request, id)
    else:
        context = {
            "blogs": Post.objects.all()
        }
        return render(request, 'blog_list.html', context)

def blog_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_detail.html', {"post": post})
    
    
