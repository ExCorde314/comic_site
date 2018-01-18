from django.urls import path
from . import views

app_name = "blog"

# url patterns for the site's blog
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:post_id>', views.single, name='single'),
    path('add', views.add, name='add'),
    path('change/<int:post_id>', views.change, name='change'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]
