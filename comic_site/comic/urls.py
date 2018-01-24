from django.urls import path
from . import views

app_name = "comic"

# The url patterns for the comic site
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:comic_id>', views.single, name='single'),
    path('add', views.add, name='add'),
    path('change/<int:comic_id>', views.change, name='change'),
    path('delete/<int:comic_id>', views.delete, name='delete'),
]