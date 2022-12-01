from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)

    phone = PhoneField()

    email = models.EmailField()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
