from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Lietotaji(models.Model):   
    REQUIRED_FIELDS = ('username',)

    username = models.OneToOneField(User, related_name='profile', unique=True)
    password = models.CharField(max_length=254)
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    class Meta:
        db_table = "lietotaji"