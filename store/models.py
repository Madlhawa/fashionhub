from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    store = models.CharField(max_length=200)

    def __str__(self):
        return self.title