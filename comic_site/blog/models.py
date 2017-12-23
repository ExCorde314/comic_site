from django.db import models
from tinymce.models import HTMLField

# Model for a blog post
class Post(models.Model):
    # Attributes for a blog post
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    content = HTMLField()

    def __str__(self):
        return self.title + " : " + self.author + " : " + str(self.date_published.date())