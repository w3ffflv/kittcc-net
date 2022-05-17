from xml.dom import ValidationErr
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValidationErr('Username is require')
        user = self.model(username = username , **extra_fields )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)    
        extra_fields.setdefault('is_superuser', True)    
        extra_fields.setdefault('is_active', True)    

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))

        return self.create_user(username , password , **extra_fields)    