from django.db import models
from author.models import Author


class Book(models.Model):
    published_at = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)