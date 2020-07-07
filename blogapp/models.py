from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

class Article(models.Model):
    title=models.CharField(max_length=250,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.title



class CustomUser(AbstractBaseUser):
    email=models.EmailField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
