from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class Lietotaji(models.Model):   
    username = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=254)
    skola = models.CharField(max_length=100)
    novads = models.CharField(max_length=100)
    skolenuskaits = models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('username',)
    class Meta:
        db_table = "lietotaji"