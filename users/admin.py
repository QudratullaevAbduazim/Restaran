from django.contrib import admin

# Register your models here.
from .models import CustomUser, Comment
admin.site.register(CustomUser)
admin.site.register(Comment)