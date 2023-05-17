from django.db import models
from django.utils import timezone
import datetime
class customer(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    Dob=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Balance = models.IntegerField(default=500)
class Transaction(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    payment_details = models.CharField(max_length=100)  # New field added
    transaction_type = models.CharField(max_length=100)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)