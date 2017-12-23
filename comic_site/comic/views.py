from django.shortcuts import render, get_object_or_404
from info.models import Info
from .models import Comic

# The home page
def index(request):
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
    }

    # Renders the result
    return render(request, 'comic/comic.html', context)

# Single view page 
def single(request, comic_id):
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
    }

    # Renders the result
    return render(request, 'comic/comic.html', context)
