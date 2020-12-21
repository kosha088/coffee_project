from django.shortcuts import render, get_object_or_404
from blog.models import Post, PostImage


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'blog/detail.html', {
        'post':post,
        'photos':photos
    })
    



