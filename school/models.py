from django.db import models

class Schoolsearch(models.Model):

    class Meta:
        db_table="auth_user"
        managed = False
        unique_together = ['skola', 'novads','skolenuskaits','apestasporcijas']
        
        skola = models.CharField(max_length=255)
        novads = models.CharField(max_length=255)
        skolenuskaits = models.CharField(max_length=255)
        apestasporcijas = models.CharField(max_length=255)