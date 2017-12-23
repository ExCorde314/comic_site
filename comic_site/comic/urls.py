from django.conf.urls import url
from . import views

app_name = "comic"

# The url patterns for the comic site
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<comic_id>[0-9]+)/$', views.single, name='single'),
]