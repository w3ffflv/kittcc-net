from operator import le, length_hint
from os import access
from pyexpat import model
from statistics import mode
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
    pirmdiena = models.TextField()
    otrdiena = models.TextField()
    tresdiena = models.TextField()
    ceturdiena = models.TextField()
    piekdiena = models.TextField()


    
    class Meta:
        db_table = "Lietotaji"