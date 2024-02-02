from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):

    username = models.CharField(max_length=30, unique=True, verbose_name="Utilisateur")
    password = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(150)])
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    
    