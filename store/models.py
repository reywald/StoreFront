from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_STATUS = [
        MEMBERSHIP_BRONZE, 'Bronze',
        MEMBERSHIP_SILVER, 'Silver',
        MEMBERSHIP_GOLD, 'Gold'
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_STATUS, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING = 'Pending'
    PAYMENT_COMPLETE = 'Complete'
    PAYMENT_FAILED = 'Failed'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'P'),
        (PAYMENT_COMPLETE, 'C'),
        (PAYMENT_FAILED, 'F')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        "Customer", on_delete=models.CASCADE, primary_key=True)
