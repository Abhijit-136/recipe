from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    Email=models.EmailField()
    adress=models.TextField()
    file=models.FileField()
    
    
    
class car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)
    