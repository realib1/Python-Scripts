from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100, blank=True)
    detail = models.CharField(max_length=255, blank=True)