from django.db import models
from django.db import connections
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class Lietotaji(AbstractBaseUser):   
   
    email = models.EmailField(User('email address'), unique=True)
    password = models.CharField(max_length=254)
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        db_table = "lietotaji"