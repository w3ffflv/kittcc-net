from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
       """
       Creates and saves a User with the given email,and password.
       """
       if not email:
            raise ValueError('Users must have an email address')
 
       user = self.model(email=self.normalize_email(email))
       user.set_password(password)
       user.save(using=self._db)
       return user
 
    def create_superuser(self, email,password=None):
       """
       Creates and saves a superuser with the given email, date of
       birth and password.
       """
       user = self.create_user(email,password=password)
       user.is_admin = True
       user.save(using=self._db)
       return user

class Lietotaji(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='email address',unique=True)
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


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Meta:
    db_table = "lietotaji"