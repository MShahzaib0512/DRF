from django.db import models

# Create your models here.

class Notes(models.Model):
 description=models.CharField(max_length=250,default="NONE") 
 
class ToDOList(models.Model):
 title=models.CharField(max_length=50)
 description=models.CharField(max_length=250)
 status=models.BooleanField(default=False)