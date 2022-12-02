from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    weight = models.IntegerField()
    image = models.ImageField()


class Cart(models.Model):
    product = models.ForeignKey(
        Product, related_name='cart', on_delete=models.CASCADE)
    user = models.ForeignKey(
        'auth.User', related_name='cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
