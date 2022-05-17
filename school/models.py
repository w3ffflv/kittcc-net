from django.db import models
from django.db import connections
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    email = None
    skola =  models.CharField(max_length=254)
    novads = models.CharField(max_length=254)
    skolenuskaits = models.CharField(max_length=10)
    apestasporcijas = models.CharField(max_length=10)
    pirmdiena = models.TextField(null=True)
    otrdiena = models.TextField(null=True)
    tresdiena = models.TextField(null=True)
    ceturdiena = models.TextField(null=True)
    piekdiena = models.TextField(null=True)
    objects = UserManager()
    USERNAME_FIELD = 'username' 

    def __unicode__(self):
        return self.user.username

        