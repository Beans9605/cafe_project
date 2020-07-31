from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser (AbstractUser) :
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    birth_day = models.DateField(default=timezone.now, null=True, blank=True)