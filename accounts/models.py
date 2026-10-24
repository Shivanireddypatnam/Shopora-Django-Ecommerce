from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=77,null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=10)
    country=models.CharField(max_length=33)

    def __str__(self):
        return f"{self.name}"

