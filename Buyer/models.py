from django.db import models

from django.db.models.deletion import CASCADE
import datetime
from Admin.models import product_tb


class Buyer_Tb(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Gender = models.CharField(max_length=20)
    Address = models.CharField(max_length=300)
    ContactNumber = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Zip = models.PositiveIntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


class Cart_Tb(models.Model):
    User = models.ForeignKey(Buyer_Tb, on_delete=CASCADE)
    Product = models.ForeignKey(product_tb, on_delete=CASCADE)
    Quantity = models.CharField(max_length=20)
    Total = models.CharField(max_length=20)
    Date = models.DateTimeField(default=datetime.datetime.now)
    Status = models.CharField(max_length=20, default="Pending")


class Order_Tb(models.Model):
    User = models.ForeignKey(Buyer_Tb, on_delete=CASCADE)
    Product = models.ForeignKey(product_tb, on_delete=CASCADE)
    Date = models.DateTimeField(default=datetime.datetime.now)
    Method = models.CharField(max_length=20, default="COD")
    Status = models.CharField(max_length=20, default="Pending")
    Quantity = models.CharField(max_length=20)
    Total = models.CharField(max_length=20)
