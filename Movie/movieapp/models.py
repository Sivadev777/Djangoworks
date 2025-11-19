from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    language = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    description = models.TextField()