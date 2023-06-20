from django.db import models

# Create your models here.
class  Trader(models.Model):
    name=models.CharField(max_length=100, default='Default Name')
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    adress=models.CharField(max_length=50)
    # products=models.ManyToManyField(product)


