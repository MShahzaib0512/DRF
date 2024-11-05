from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Notes(models.Model):
 description=models.CharField(max_length=250,default="NONE") 
 
class ToDOList(models.Model):
 title=models.CharField(max_length=50)
 description=models.CharField(max_length=250)
 status=models.BooleanField(default=False)
 
class ContactManagement(models.Model):
 name=models.CharField(max_length=50)
 phone=PhoneNumberField(verbose_name="Enter your contat number")
 email=models.EmailField(max_length=254)