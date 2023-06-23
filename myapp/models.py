from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import UserManager
# Create your models here.


class User(AbstractUser):

    user_choise= [
        ('seller','seller'),
        ('buyer','buyer'),
    ]

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    user_type = models.CharField(max_length=6,choices=user_choise,default="buyer",null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

