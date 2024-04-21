from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#Models to define database layout and layout info to be stored

class Recipe(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     ingredients = models.TextField(default = '')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.title
     
     def save(self, *args, **kwargs):
        # Call the superclass's save method to save the instance
        super().save(*args, **kwargs)
    
        
    


