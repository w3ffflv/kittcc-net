from django.db import models
from django.db import connections

class Student(models.Model):   
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    apestasporcijas = models.CharField(max_length=100)
    access = models.CharField(max_length=1)
    pirmdiena = models.TextField(null=True)
    otrdiena = models.TextField(null=True)
    tresdiena = models.TextField(null=True)
    ceturdiena = models.TextField(null=True)
    piekdiena = models.TextField(null=True)
    class Meta:
        db_table = "Lietotaji"