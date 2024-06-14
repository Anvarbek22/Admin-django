from django.db import models


class Maxsulotlar(models.Model):
    name=models.CharField(max_length=255)
    url=models.CharField(max_length=255,null=True)
    destrib=models.TextField()
    img=models.ImageField(upload_to="image/")


class Userss(models.Model):
    UN=models.CharField(max_length=255)
    PN=models.CharField(max_length=255)
    TS=models.CharField(max_length=255)
    CM=models.CharField(max_length=255)
    P=models.CharField(max_length=255)
    M=models.CharField(max_length=255)

# Create your models here.
