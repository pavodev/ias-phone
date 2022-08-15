from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)