from django.db import models

class School(models.Model):
    skola = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'