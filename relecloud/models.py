from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=False)
    slug =models.SlugField()