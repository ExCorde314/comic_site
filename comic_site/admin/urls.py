from django.conf.urls import url
from . import views

app_name = "admin"

# The url patterns for the admin
urlpatterns = [
    url(r'^$', views.admin_panel, name='admin-panel'),
    url(r'^login$', views.login_page, name='login'),
    url(r'^logout$', views.logout_page, name='logout'),
]