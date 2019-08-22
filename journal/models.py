from django.db import models

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
