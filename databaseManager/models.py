from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#Models to define database layout and layout info to be stored


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    numRecipes = models.IntegerField(default = 0)

class Recipe(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()

     author = models.ForeignKey(User, on_delete=models.CASCADE)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.title
    
        
    


