from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError('Phone Number is required')
        
        user = self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        return self.create_user(phone,password,**extra_fields)



class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=12,unique=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    