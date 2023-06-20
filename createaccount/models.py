from django.db import models

# Create your models here.

class new_user (models.Model):


    username = models.CharField(max_length = 32,default='Default Name')
    userId=models.IntegerField()
    email=models.CharField(max_length=50)
    firstname=models.CharField(max_length=32)
    lastname=models.CharField(max_length=32)
    dateofbirth=models.DateField()
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name

