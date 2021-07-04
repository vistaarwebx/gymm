from django.db import models
from djrichtextfield.models import RichTextField


class contactss(models.Model):
    name = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True,blank=False)
    Email = models.EmailField(null=True)
    message = models.TextField(null=True)

class Blog(models.Model):
    image = models.FileField(null=True)
    heading = models.CharField(max_length=30,null=True)
    detail = models.TextField(null=True)
    category = models.CharField(max_length=30,null=True)
    date = models.DateField(auto_now=True,null=True)
    message = models.TextField(null=True)
    content = RichTextField(null=True)

class Gallery(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    discription = models.TextField(null=True)


class Services(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    discription = models.TextField(null=True)