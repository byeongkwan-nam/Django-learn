from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Custom User """

    GENDER_MEN = "men"
    GENDER_WOMEN = "women"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = (
        (GENDER_MEN, "Man"),
        (GENDER_WOMEN, "Woman"),
        (GENDER_OTHER, "Other")
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default='', blank=True)


