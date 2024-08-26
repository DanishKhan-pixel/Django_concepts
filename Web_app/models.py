from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    collage = models.CharField(max_length=30)
    age=models.IntegerField(max_length=30)
    is_active=models.BooleanField(default=True)