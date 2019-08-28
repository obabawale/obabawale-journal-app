from django.db import models
from django.contrib.auth.models import User


class Journal(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journal_author", default=1)

    def __str__(self):
        return f"{self.title}: {self.body}"