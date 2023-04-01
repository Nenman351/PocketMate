from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Card(models.Model):
    card_name = models.CharField(max_length=255, blank=False, null=False)
    card_number = models.IntegerField()
    expiry_date = models.DateField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.card_name


class Next_Of_Kin(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    relationship = models.CharField(max_length=255, blank=False, null=False)
    bvn = models.IntegerField()

    def __str__(self):
        return self.full_name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    next_0f_kin = models.ForeignKey(Next_Of_Kin, on_delete=models.CASCADE, related_name='next_of_kin')
    home_address = models.CharField(max_length=255)
    nin = models.IntegerField(blank=False, null=False)


class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')


class Status(Enum):
    SUCCESSFUL = 'Successful'
    PENDING = 'Pending'
    FAILED = 'Failed'
    REVERSED = 'Reversed'


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Deposit', 'D'),
        ('Withdrawal', 'W'),
        ('Transfer', 'T'),
    )
    STATUS_CHOICES = [(status.name, status.value) for status in Status]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=45, choices=STATUS_CHOICES, default='success')
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Transaction #{self.pk}'
