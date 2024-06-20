# api/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    google_sub = models.CharField(max_length=255, blank=True, null=True, unique=True)  
