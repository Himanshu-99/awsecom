from django.db import models

class ProductModel(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    photo = models.FileField()

