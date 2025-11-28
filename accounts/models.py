from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField(blank=True,null=True)
    name=models.CharField(max_length=40,null=True,blank=True)
    image=models.ImageField(default='placeholder.jpg',upload_to='images')
    address=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.username - {(self.phone_number)}