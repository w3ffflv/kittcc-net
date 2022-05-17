from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Lietotaji(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    apestasporcijas = models.CharField(max_length=100)
    pirmdiena = models.TextField()
    otrdiena = models.TextField()
    tresdiena = models.TextField()
    ceturdiena = models.TextField()
    piekdiena = models.TextField()
    class Meta:
        db_table = "Lietotaji"

        