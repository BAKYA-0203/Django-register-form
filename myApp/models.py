from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dateonbirth=models.CharField(max_length=100)
    bloodgroup=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

