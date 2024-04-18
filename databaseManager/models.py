from django.db import models
from django.utils import timezone

# Create your models here.
#Models to define database layout and layout info to be stored

#save username to database
class saveUsername(models.Model):
    username = models.CharField(max_length=50)
    log_date = models.DateTimeField("date logged")

