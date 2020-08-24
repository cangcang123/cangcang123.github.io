from django.db import models
from django.conf import settings
class Namprod(models.Model):
    name = models.CharField(max_length=50,null=True)
class Prodtype(models.Model):
    name = models.CharField(max_length=50,null=True)
    idname = models.ForeignKey(Namprod, on_delete=models.CASCADE) #khoa ngoai cua Nameprod
class Productype(models.Model):
    name = models.CharField(max_length=50,null=True)
    idname = models.ForeignKey(Namprod, on_delete=models.CASCADE)
    idpro= models.ForeignKey(Prodtype, on_delete=models.CASCADE)
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=100)
    GB = models.IntegerField(max_length=11)
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    idpro = models.ForeignKey(Namprod, on_delete=models.CASCADE)
    idtype = models.ForeignKey(Productype, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
class pro_image(models.Model):
    name = models.CharField(max_length=50)
    pro_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    # Create your models here.
class Test1(models.Model):
    name = models.CharField(max_length=10)
class Test2(models.Model):
    name = models.CharField(max_length=10)
class Giohang(models.Model):
    iduser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50,null=True)
    soluong = models.IntegerField(max_length=11,null=True)
    gia = models.CharField(max_length=30,null=True)
    date = models.DateTimeField(auto_now_add=True)

