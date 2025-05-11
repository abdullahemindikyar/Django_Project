from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
    favoriler = models.ManyToManyField(User, related_name="favori_filmler", blank=True)
    begenenler = models.ManyToManyField(User, related_name="begendigi_filmler", blank=True)
    begenmeyenler = models.ManyToManyField(User, related_name="begenmedigi_filmler", blank=True)
