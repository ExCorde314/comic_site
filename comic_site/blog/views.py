from django.shortcuts import render, get_object_or_404
from info.models import Info
from .models import Post

# The landing page of the blog
def index(request):
    # Gets the latest and first blog posts
    post = Post.objects.filter(date_published__isnull=False).latest('date_published')
    earliest = Post.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.objects.order_by('site_name')[0]

    # Gets the next and previous post
    try:
        next_post = post.get_next_by_date_published().id
    except Post.DoesNotExist:
        next_post = post.id
    try:
        previous_post = post.get_previous_by_date_published().id
    except Post.DoesNotExist:
        previous_post = post.id

    # Prepares the context for the page
    context = {
        'post': post,
        'first': earliest.id,
        'next': next_post,
        'previous': previous_post,
        'info': info,
    }

    # Renders the result
    return render(request, 'blog/single_post.html', context)

# Single blog post page
def single(request, post_id):
    # Gets the current post and the first post
    post = get_object_or_404(Post, pk=post_id)
    earliest = Post.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.objects.order_by('site_name')[0]

    # Gets the next and previous post
    try:
        next_post = post.get_next_by_date_published().id
    except Post.DoesNotExist:
        next_post = post.id
    try:
        previous_post = post.get_previous_by_date_published().id
    except Post.DoesNotExist:
        previous_post = post.id

    # Prepares the context for the page
    context = {
        'post': post,
        'first': earliest.id,
        'next': next_post,
        'previous': previous_post,
        'info': info,
    }

    # Renders the result
    return render(request, 'blog/single_post.html', context)
