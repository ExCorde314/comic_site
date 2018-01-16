from django.conf.urls import url
from . import views

app_name = "comic"

# The url patterns for the comic site
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<comic_id>[0-9]+)$', views.single, name='single'),
    url(r'^add$', views.add, name='add'),
    url(r'^change/(?P<comic_id>[0-9]+)$', views.change, name='change'),
    url(r'^delete/(?P<comic_id>[0-9]+)$', views.delete, name='delete'),
]