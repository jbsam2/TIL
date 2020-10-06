from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)