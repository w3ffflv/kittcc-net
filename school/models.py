from os import access
from django.db import models

class Edienkarte(models.Model):
        
        skola = models.CharField(max_length=255,default='',null=False)
        novads = models.CharField(max_length=255,default='',null=False)
        skolenuskaits = models.CharField(max_length=255,default='',null=False)
        access_code = models.CharField(max_length=255,default='',null=False)
        appestas_porcijas = models.CharField(max_length=255,default='',null=False)
        pirmdiena = models.CharField(max_length=255,default='',null=False)
        otrdiena = models.CharField(max_length=255,default='',null=False)
        tresdiena = models.CharField(max_length=255,default='',null=False)
        ceturdiena = models.CharField(max_length=255,default='',null=False)
        piekdiena = models.CharField(max_length=255,default='',null=False)
        
        