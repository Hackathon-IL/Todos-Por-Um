from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=100,blank=True, default='')
    description = models.CharField(max_length=200, blank=False, default='')

