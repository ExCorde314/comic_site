from django.urls import path
from . import views

app_name = "admin"

# The url patterns for the admin
urlpatterns = [
    path('', views.admin_panel, name='admin-panel'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
]