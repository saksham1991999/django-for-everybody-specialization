from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    area_hectares = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    justification = models.TextField()
    description = models.TextField()


    def __str__(self) :
        return self.name