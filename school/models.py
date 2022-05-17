from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Lietotaji(models.Model):
    access= models.ForeignKey(User, on_delete=models.CASCADE)
    skola =  models.CharField(max_length=254)
    novads = models.CharField(max_length=254)
    skolenuskaits = models.CharField(max_length=254)
    apestasporcijas = models.CharField(max_length=254)
    pirmdiena = models.TextField()
    otrdiena = models.TextField()
    tresdiena = models.TextField()
    ceturdiena = models.TextField()
    piekdiena = models.TextField()
    class Meta:
        db_table = "Lietotaji"

        