from django.db import models


# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    currency = models.CharField(max_length=5)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f'{self.id}'