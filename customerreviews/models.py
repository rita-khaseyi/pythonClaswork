from django.db import models

# Create your models here.

class Review(models.Model):
    product = models.CharField(max_length = 32)
    rating=models.IntegerField()
    comment=models.TextField()
 
    def __str__(self):
        return self.name
