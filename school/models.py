from django.db import models
from django.db import connections

class Lietotaji(models.Model):   
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    class Meta:
        db_table = "lietotaji"