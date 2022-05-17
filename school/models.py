from django.db import models
from django.db import connections

class Student(models.Model):   
    
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    apestasporcijas = models.CharField(max_length=100)

    
    class Meta:
        db_table = "Lietotaji"