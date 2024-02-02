from django.db import models
from django.conf import settings
from authentication.models import *

class Project(models.Model):
    class Type(models.TextChoices):
        BACK_END = 'back_end'
        FRONT_END = 'front_end'
        IOS = 'IOS'
        ANDROID = 'android'
    
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='author')
    contributors = models.ManyToManyField(User)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=Type.choices)
    created_time = models.DateTimeField(auto_now_add=True)
