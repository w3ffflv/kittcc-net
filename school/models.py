from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user



class Lietotaji(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=254)
    repassword = models.CharField(max_length=254)
    skola = models.CharField(max_length=254, unique=True)
    skolenuskaits = models.CharField(max_length=254)
    novads = models.CharField(max_length=254)
    apestasporcijas = models.CharField(max_length=254)
    pirmdiena = models.CharField(max_length=254)
    otrdiena = models.CharField(max_length=254)
    tresdiena = models.CharField(max_length=254)
    ceturdiena = models.CharField(max_length=254)
    piekdiena = models.CharField(max_length=254)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']    

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
	    return self.is_admin

class Meta:
    db_table = "lietotaji"