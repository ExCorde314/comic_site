from django.conf.urls import url
from . import views

app_name = "info"

# The url patterns for the admin
urlpatterns = [
    url(r'^login$', views.login_page, name='login'),
    url(r'^logout$', views.logout_page, name='logout'),
]