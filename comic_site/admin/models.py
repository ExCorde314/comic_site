from django.db import models

# Model for keeping track of people who are authorized to make a new account
class RegisterAuth(models.Model):
    # The email that is allowed to register
    email = models.CharField(max_length=200, default="")

    # Permissions that the user will have
    comic_add = models.BooleanField(default=False)
    comic_change = models.BooleanField(default=False)
    comic_delete = models.BooleanField(default=False)
    post_add = models.BooleanField(default=False)
    post_change = models.BooleanField(default=False)
    post_delete = models.BooleanField(default=False)
    user_add = models.BooleanField(default=False)
    user_chage = models.BooleanField(default=False)
    user_delete = models.BooleanField(default=False)
    info_change = models.BooleanField(default=False)
