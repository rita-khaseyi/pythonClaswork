from django.db import models

# Create your models here.


class cart(models.Model):
    product=models.CharField(max_length=32)
    userId=models.IntegerField()
    totalprice=models.DecimalField(max_digits = 6,decimal_places = 2)
    quantity=models.IntegerField()
def __str__(self):
    return self.name    




