from django.db import models

# Create your models here.

class Contacts(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    email = models.CharField(max_length=200)
