from django.db import models

# Create your models here.

class Order_request (models.Model):

    name = models.CharField(max_length = 32,default='Default Name')
    userId=models.IntegerField()
    total_amount=models.DecimalField(max_digits = 6,decimal_places = 2)
    # shipping_Adress=models.CharField(max_length=60)
    order_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


  


