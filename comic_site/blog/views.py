from django.shortcuts import render, get_object_or_404, redirect
from info.models import Info
from .models import Post
from .forms import AddPost, ChangePost
from django.http import Http404

# The landing page of the blog
def index(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated
    
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
        'user_logged_in': user_logged_in,
    }

    # Renders the result
    return render(request, 'blog/single.html', context)

# Single blog post page
def single(request, post_id):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

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
        'user_logged_in': user_logged_in,
    }

    # Renders the result
    return render(request, 'blog/single.html', context)

def add(request):
    if not request.user.is_authenticated or not request.user.has_perm('blog.add_post'):
        raise Http404

    if request.method == "POST":
        form = AddPost(request.POST)

        if not form.is_valid():
            # Prepares the context for the page
            info = Info.objects.order_by('site_name')[0]
            context = {
                'info': info,
                'user_logged_in': True,
                'form': form,
            }

            return render(request, 'blog/add.html', context)

        form.save()
        return redirect('blog:index')
    
    info = Info.objects.order_by('site_name')[0]
    form = AddPost()

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
        'form': form,
    }

    return render(request, 'blog/add.html', context)

def change(request):
    context = {}
    return render(request, 'blog/change.html', context)

def delete(request):
    context = {}
    return render(request, 'blog/delete.html', context)