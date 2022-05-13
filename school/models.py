from django.db import models

# Create your models here.

class Details(models.Model):
    skola = models.CharField(max_length=205, default='', null=False)
    skolenuskaits = models.CharField(max_length=222, default='', null=False)
