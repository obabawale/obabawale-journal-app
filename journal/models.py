from django.db import models

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=3)
    body = models.CharField(max_length=64)
