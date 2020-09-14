from django.db import models
from django.urls import reverse

# Create your models here.
class IoTListModel(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    abstract=models.TextField()
    diagram=models.ImageField(default='default.png',blank=True)
    cost=models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('detail',args=[self.slug])

class CheckoutModel(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    phno=models.CharField(max_length=15)
    # date=models.DateField()
    Orderdate=models.DateTimeField(auto_now=True)
    Email=models.EmailField()

class Idea(models.Model):
    name=models.CharField(max_length=100)
    phno=models.CharField(max_length=15)
    # Submitteddate=models.DateTimeField(auto_now=True)
    Email=models.EmailField()
    message=models.TextField()
    diagram=models.ImageField(default='default.png',blank=True, null=True)
