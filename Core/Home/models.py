from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    gender = models.CharField(max_length=10)


