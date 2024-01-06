from django.db import models
from django.contrib.auth.models import AbstractUser

# how can i implement encrypted password in api


class User(AbstractUser):
    pass


class Reservation(models.Model):
    vehicle_name = models.CharField(max_length=256)
    name = models.CharField(max_length=27)
    email = models.EmailField()
    contact_number = models.BigIntegerField()
    payment_method = models.TextField()
    insurance_plan = models.TextField()
    warranty = models.TextField()
    service_maintenance = models.TextField()
    comment = models.TextField(blank=True)
    received_email = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
