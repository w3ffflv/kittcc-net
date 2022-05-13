from os import access
from django.db import models

class School(models.Model):



    username = models.CharField(max_length=205,default='', null=False)
    password = models.CharField(max_length=205,default='', null=False)
    skola = models.CharField(max_length=205,default='', null=False)
    novads = models.CharField(max_length=205,default='', null=False) 
    skolenuskaits = models.CharField(max_length=205,default='', null=False) 
    apestas_porcijas = models.CharField(max_length=205,default='', null=False) 
    pirmdiena = models.CharField(max_length=205,default='', null=False) 
    otrdiena = models.CharField(max_length=205,default='', null=False) 
    tresdiena = models.CharField(max_length=205,default='', null=False) 
    ceturdiena = models.CharField(max_length=205,default='', null=False)  
    piekdiena = models.CharField(max_length=205,default='', null=False) 

        