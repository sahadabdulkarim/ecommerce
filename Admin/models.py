from django.db import models


class Admin_Tb(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


class Category_Tb(models.Model):
    Name = models.CharField(max_length=30)


class product_tb(models.Model):
    Category = models.ForeignKey(Category_Tb, on_delete=models.CASCADE)
    Admin = models.ForeignKey(Admin_Tb, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    Details = models.CharField(max_length=20)
    Quantity = models.CharField(max_length=20)
    Image = models.FileField(upload_to="%Y%m%d")
