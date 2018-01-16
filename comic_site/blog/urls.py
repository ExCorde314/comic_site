from django.conf.urls import url
from . import views

app_name = "blog"

# url patterns for the site's blog
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<post_id>[0-9]+)$', views.single, name='single'),
    url(r'^add$', views.add, name='add'),
    url(r'^change/(?P<post_id>[0-9]+)$', views.change, name='change'),
    url(r'^delete/(?P<post_id>[0-9]+)$', views.delete, name='delete'),
]
