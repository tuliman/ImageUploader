from django.db import models


# Create your models here.

class Images(models.Model):
    image = models.ImageField(blank=True)



class Size(models.Model):
    img = models.ForeignKey('Images', on_delete=models.CASCADE)
    width = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
