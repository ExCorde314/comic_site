from django.shortcuts import render, get_object_or_404, redirect
from info.models import Info
from .models import Comic
from .forms import AddComic, ChangeComic
from django.http import Http404

# The home page
def index(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated
    
    # Gets the latest and first comics
    comic = Comic.objects.filter(date_published__isnull=False).latest('date_published')
    earliest = Comic.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.objects.order_by('site_name')[0]

    # Gets the next and previous comic
    try:
        next_post = comic.get_next_by_date_published().id
    except Comic.DoesNotExist:
        next_post = comic.id

    try:
        previous_post = comic.get_previous_by_date_published().id
    except Comic.DoesNotExist:
        previous_post = comic.id

    # Prepares the context for the page
    context = {
        'comic': comic,
        'first': earliest.id,
        'next': next_post,
        'previous': previous_post,
        'info': info,
        'user_logged_in': user_logged_in,
    }

    # Renders the result
    return render(request, 'comic/comic.html', context)

# Single view page 
def single(request, comic_id):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    # Gets the current comic and the first comic
    comic = get_object_or_404(Comic, pk=comic_id)
    earliest = Comic.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.objects.order_by('site_name')[0]

    # Gets the next and previous comic
    try:
        next_post = comic.get_next_by_date_published().id
    except Comic.DoesNotExist:
        next_post = comic.id
    try:
        previous_post = comic.get_previous_by_date_published().id
    except Comic.DoesNotExist:
        previous_post = comic.id

    # Prepares the context for the page
    context = {
        'comic': comic,
        'first': earliest.id,
        'next': next_post,
        'previous': previous_post,
        'info': info,
        'user_logged_in': user_logged_in,
    }

    # Renders the result
    return render(request, 'comic/comic.html', context)

def add(request):
    if not request.user.is_authenticated or not request.user.has_perm('comic.add_comic'):
        raise Http404

    if request.method == "POST":
        form = AddComic(request.POST, request.FILES)

        if not form.is_valid():
            # Prepares the context for the page
            info = Info.objects.order_by('site_name')[0]
            context = {
                'info': info,
                'user_logged_in': True,
                'form': form,
            }

            return render(request, 'comic/add.html', context)

        form.save()
        return redirect('admin:admin-panel')


    info = Info.objects.order_by('site_name')[0]
    form = AddComic()

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
        'form': form,
    }

    return render(request, 'comic/add.html', context)

def change(request, comic_id):
    if not request.user.is_authenticated or not request.user.has_perm("comic.change_comic"):
        raise Http404
    
    info = Info.objects.order_by('site_name')[0]

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
    }

    return render(request, 'comic/comic_edit.html', context)

def delete(request, comic_id):
    if not request.user.is_authenticated or not request.user.has_perm("comic.delete_comic"):
        raise Http404
    
    info = Info.objects.order_by('site_name')[0]

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
    }

    return render(request, 'comic/comic_edit.html', context)