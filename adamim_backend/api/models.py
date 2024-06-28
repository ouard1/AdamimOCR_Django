from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    google_sub = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        app_label = 'api'
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        verbose_name = 'User'
        verbose_name_plural = 'Users'
