from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=13,default='')
    CHOICES = (
        (1,'admin'),
        (2,'adib'),
        (3,'user'),
    )
    user_roles = models.PositiveIntegerField(default=1,choices=CHOICES)