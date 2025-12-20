from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

from myapp.models import Food


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')


    def __str__(self):
        return self.username

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
