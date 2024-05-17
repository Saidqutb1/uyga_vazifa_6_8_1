from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    image = models.ImageField(upload_to='user_image/', blank=True, null=True, default='default_img/download.pgn')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

