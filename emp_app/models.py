from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)


class Car(models.Model):
    carname=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)
       