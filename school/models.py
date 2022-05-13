from django.db import models

class Edienkarte(models.Model):
        pirmdiena = models.CharField(max_length=255,default='',null=False)
        otrdiena = models.CharField(max_length=255,default='',null=False)
        tresdiena = models.CharField(max_length=255,default='',null=False)
        ceturdiena = models.CharField(max_length=255,default='',null=False)
        piekdiena = models.CharField(max_length=255,default='',null=False)
        