from audioop import maxpp
import email
from email import message
from unicodedata import name
from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    date = models.DateTimeField()
    time = models.TimeField()
    people = models.CharField(max_length=100)
    message = models.CharField(max_length=700) 

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     subject = models.CharField(max_length=500)
#     message = models.CharField(max_length=500) 

