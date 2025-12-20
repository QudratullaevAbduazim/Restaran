from django.conf import settings
from django.db import models

class Food(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='foods'
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

