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

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    LANGUAGE_US = "us"
    LANGUAGE_KR = "kr"
    LANGUAGE_CHOICES = (
        (LANGUAGE_US, "US"),
        (LANGUAGE_KR, "KR")
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default='', blank=True)


    birthdate = models.DateField(null=True)
    currency = models.CharField(null=True, blank=True, max_length=3, choices=CURRENCY_CHOICES)
    language = models.CharField(null=True, blank=True, max_length=2, choices=LANGUAGE_CHOICES)
    superhost = models.BooleanField(default=False)


