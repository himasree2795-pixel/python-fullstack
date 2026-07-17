from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CoustmUser(AbstractUser):
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username