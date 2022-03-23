from distutils.command.upload import upload
import email
from email import message
from pyexpat import model
from turtle import title
from django.conf import settings
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User
from django.forms import SlugField
# Create your models here.

class Carausal(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    subtitle=models.TextField()
    
    def __str__(self):
        return self.title

class Shop(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    subtitle=models.TextField()
    slug = models.SlugField(max_length=50,null=True)
    
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    subtitle=models.TextField()
    
    def __str__(self):
        return self.title
    
class Offer(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    photo = models.ImageField(upload_to ='images')
    pic = models.ImageField(upload_to ='images')
    subtitle=models.TextField()
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title=models.CharField(max_length=100)
    title2=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    photo = models.ImageField(upload_to ='images')
    subtitle=models.TextField()
    subtitle2=models.TextField()
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    subtitle=models.TextField()
    
    def __str__(self):
        return self.title
    

class Info(models.Model):
    title=models.CharField(max_length=100)
    title2=models.CharField(max_length=100)
    title3=models.CharField(max_length=100)
    title4=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images')
    subtitle=models.TextField()
    subtitle2=models.TextField()
    subtitle3=models.TextField()
    
    def __str__(self):
        return self.title  
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    message=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Shopcat(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    photos=models.ImageField(upload_to='images')
    



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.title



class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title

   