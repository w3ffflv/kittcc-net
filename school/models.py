from os import access
from django.db import models

class School(models.Model):
    skola = models.CharField(max_length=255,default='',null=False)