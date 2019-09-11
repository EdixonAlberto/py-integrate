from django.db import models

# Create your models here.
class Equations(models.Model):
    name = models.CharField(max_length=20)
    equation = models.TextField()
