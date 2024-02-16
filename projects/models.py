from django.db import models
from django.conf import settings
from authentication.models import *
import uuid

class Project(models.Model):
    class Type(models.TextChoices):
        BACK_END = 'back_end'
        FRONT_END = 'front_end'
        IOS = 'IOS'
        ANDROID = 'android'
    
    name = models.CharField(max_length=30)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', blank=True)
    contributors = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=Type.choices)
    created_time = models.DateTimeField(auto_now_add=True)

class Issue(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'high'
        MEDIUM = 'medium'
        LOW = 'low'
    class Status(models.TextChoices):
        TO_DO = 'to_do'
        IN_PROGRESS = 'in_progress'
        FINISHED = 'finished'
    class Tag(models.TextChoices):
        BUG = 'bug'
        FEATURE = 'feature'
        TASK = 'task'
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, related_name='project_id')
    name = models.CharField(max_length=20)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_author', null=True)
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='assigned_to', blank=True, null=True)
    description = models.TextField(max_length=150, blank=True)
    priority = models.CharField(max_length=20, choices=Priority.choices)
    tag = models.CharField(max_length=20, choices=Tag.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default='to_do')
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
