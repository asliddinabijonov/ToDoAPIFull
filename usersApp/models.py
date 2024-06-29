from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
