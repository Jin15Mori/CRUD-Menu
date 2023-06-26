from django.db import models

# Create your models here.
class Home(models.Model):
    foodname = models.CharField(max_length=255, null=True)
    foodcost = models.CharField(max_length=255, null=True)
    foodtype = models.CharField(max_length=255, null=True)
    
