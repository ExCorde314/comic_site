from django.db import models

# A definition of a singleton model for use here
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

# A singleton class that contains site-wide information
class Info(SingletonModel):
    site_name = models.CharField(max_length=200, default=" ")
    charset = models.CharField(max_length=200, default=" ")
    logo = models.ImageField(upload_to='images')
    about = models.CharField(max_length=200, default="This comic is about ordinary, scientific, mathmatical, intriguing, and downright strange things and contains some interesting characters.")

# A singleton class that contains 400 error page information
class Info400(SingletonModel):
    title = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to='images')
    image_width = models.CharField(max_length=200, default=" ")
    image_height = models.CharField(max_length=200, default=" ")
    title_text = models.CharField(max_length=200, default=" ")
    alt_text = models.CharField(max_length=200, default=" ")
    message = models.CharField(max_length=200, default=" ")

# A singleton class that contains 404 error page information
class Info404(SingletonModel):
    title = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to='images')
    image_width = models.CharField(max_length=200, default=" ")
    image_height = models.CharField(max_length=200, default=" ")
    title_text = models.CharField(max_length=200, default=" ")
    alt_text = models.CharField(max_length=200, default=" ")
    message = models.CharField(max_length=200, default=" ")

# A singleton class that contains 403 error page information
class Info403(SingletonModel):
    title = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to='images')
    image_width = models.CharField(max_length=200, default=" ")
    image_height = models.CharField(max_length=200, default=" ")
    title_text = models.CharField(max_length=200, default=" ")
    alt_text = models.CharField(max_length=200, default=" ")
    message = models.CharField(max_length=200, default=" ")

# A singleton class that contains 500 error page information
class Info500(SingletonModel):
    title = models.CharField(max_length=200, default=" ")
    image = models.ImageField(upload_to='images')
    image_width = models.CharField(max_length=200, default=" ")
    image_height = models.CharField(max_length=200, default=" ")
    title_text = models.CharField(max_length=200, default=" ")
    alt_text = models.CharField(max_length=200, default=" ")
    message = models.CharField(max_length=200, default=" ")
