from django.db import models

# Create your models here.

class User(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    