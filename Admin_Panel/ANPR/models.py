from django.db import models
from phone_field import PhoneField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30)
    mobile_no=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    amount=models.BigIntegerField(default=0)
    paymentDone=models.BooleanField()

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name=models.CharField(max_length=30)
    number_plate=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name