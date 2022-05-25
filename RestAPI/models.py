from django.db import models
from djgeojson.fields import PointField

# Create your models here.


class Provider(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Language = models.CharField(max_length=25)
    Currency = models.CharField(max_length=10)


class ServiceArea(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.FloatField()
    Location = PointField()
