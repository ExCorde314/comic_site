from django.db import models

# Models
class Comic(models.Model):
    # Comic Attributes
    title = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to=".")
    image_width = models.CharField(max_length=200, default=" ")
    image_height = models.CharField(max_length=200, default=" ")
    title_text = models.CharField(max_length=200, default=" ")
    alt_text = models.CharField(max_length=200, default=" ")
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+ ': ' + self.title + ' : ' + str(self.date_published.date())