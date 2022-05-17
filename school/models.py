from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Skolas(models.Model):
    
    skola = models.ForeignKey(User, on_delete=models.CASCADE)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    apestasporcijas = models.CharField(max_length=100)
    pirmdiena = models.TextField()
    otrdiena = models.TextField()
    tresdiena = models.TextField()
    ceturdiena = models.TextField()
    piekdiena = models.TextField()
    class Meta:
        db_table = "Skolas"

        