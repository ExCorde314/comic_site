from django.shortcuts import render, get_object_or_404, redirect
from info.models import Info
from .models import Comic
from .forms import AddComic, ChangeComic, DeleteComic
from django.http import Http404

# The home page
def index(request):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated
    
    # Gets the latest and first comics
    comic = Comic.objects.filter(date_published__isnull=False).latest('date_published')
    earliest = Comic.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.load()

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
    return render(request, 'comic/single.html', context)

# Single view page 
def single(request, comic_id):
    # Gets whether or not the user is logged in
    user_logged_in = request.user.is_authenticated

    # Gets the current comic and the first comic
    comic = get_object_or_404(Comic, pk=comic_id)
    earliest = Comic.objects.filter(date_published__isnull=False).earliest('date_published')
    info = Info.load()

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
    return render(request, 'comic/single.html', context)

def add(request):
    if not request.user.is_authenticated or not request.user.has_perm('comic.add_comic'):
        raise Http404

    if request.method == "POST":
        form = AddComic(request.POST, request.FILES)

        if not form.is_valid():
            # Prepares the context for the page
            info = Info.load()
            context = {
                'info': info,
                'user_logged_in': True,
                'form': form,
            }

            return render(request, 'comic/add.html', context)

        form.save()
        return redirect('admin:admin-panel')


    info = Info.load()
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

    comic = get_object_or_404(Comic, pk=comic_id)

    if request.method == "POST":
        form = ChangeComic(request.POST, instance=comic)

        if not form.is_valid():
            # Prepares the context for the page
            info = Info.load()
            context = {
                'info': info,
                'user_logged_in': True,
                'form': form,
                'comic': comic,
            }

            return render(request, 'comic/change.html', context)

        form.save()
        return redirect('comic:single', comic_id=comic_id)

    info = Info.load()
    form = ChangeComic(instance=comic)

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
        'form': form,
        'comic': comic,
    }

    return render(request, 'comic/change.html', context)

def delete(request, comic_id):
    if not request.user.is_authenticated or not request.user.has_perm("comic.delete_comic"):
        raise Http404
    
    comic = get_object_or_404(Comic, pk=comic_id)

    if request.method == "POST":
        form = DeleteComic(request.POST)

        if not form.is_valid():
            # Prepares the context for the page
            info = Info.load()
            context = {
                'info': info,
                'user_logged_in': True,
                'form': form,
                'comic': comic,
            }

            return render(request, 'comic/delete.html', context)

        comic.delete()
        return redirect('comic:index')
    
    info = Info.load()
    form = DeleteComic()

    # Prepares the context for the page
    context = {
        'info': info,
        'user_logged_in': True,
        'form': form,
        'comic': comic,
    }

    return render(request, 'comic/delete.html', context)