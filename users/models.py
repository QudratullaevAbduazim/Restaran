from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')


    def __str__(self):
        return self.username
