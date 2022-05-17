from django.db import models
from django.db import connections
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skola =  models.CharField(max_length=254)
    novads = models.CharField(max_length=254)
    skolenuskaits = models.CharField(max_length=254)
    apestasporcijas = models.CharField(max_length=254)
    pirmdiena = models.TextField()
    otrdiena = models.TextField()
    tresdiena = models.TextField()
    ceturdiena = models.TextField()
    piekdiena = models.TextField()

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Profils'
        verbose_name_plural = 'Profils'
        