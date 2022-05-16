from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Lietotaji(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=254)
    repassword = models.CharField(max_length=254)
    skola = models.CharField(max_length=254, unique=True)
    skolenuskaits = models.CharField(max_length=254)
    novads = models.CharField(max_length=254)
    apestasporcijas = models.CharField(max_length=254)
    pirmdiena = models.CharField(max_length=254)
    otrdiena = models.CharField(max_length=254)
    tresdiena = models.CharField(max_length=254)
    ceturdiena = models.CharField(max_length=254)
    piekdiena = models.CharField(max_length=254)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['skola']    
    def __str__(self) -> str:
        return self.username
    class Meta:
        db_table = "lietotaji"