from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    CATEGORY = (
        ('C', 'Clothing and shoes'),
        ('M', 'Motorcycle'),
        ('P', 'Computer equipment')
    )
    CONDITION = (
        ('N', 'New' ),
        ('R', 'Refurbished'),
        ('U', 'Used')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORY)
    condition = models.CharField(max_length=50, choices=CONDITION)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class History(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()
