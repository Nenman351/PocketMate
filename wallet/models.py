from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Card(models.Model):
    card_name = models.CharField(max_length=255, blank=False, null=False)
    card_number = models.CharField(max_length=255, blank=False, null=False)
    expiry_date = models.DateField(blank=False, null=False)
    cvv = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return self.card_name


class Next_Of_Kin(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    relationship = models.CharField(max_length=255, blank=False, null=False)
    bvn = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.full_name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)
    next_0f_kin = models.OneToOneField(Next_Of_Kin, on_delete=models.CASCADE, null=True, related_name='next_0f_kin')
    home_address = models.CharField(max_length=255)
    nin = models.CharField(max_length=20, blank=False, null=False)
    profile_image = models.ImageField(upload_to='media/images')


class Account(models.Model):
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Status(Enum):
    SUCCESSFUL = 'Successful'
    PENDING = 'Pending'
    FAILED = 'Failed'
    REVERSED = 'Reversed'


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Deposit', 'deposit'),
        ('Transfer', 'transfer'),
    )
    STATUS_CHOICES = [(status.name, status.value) for status in Status]
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()
    status = models.CharField(max_length=45, choices=STATUS_CHOICES, default='success')
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Transaction #{self.pk}'


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='beneficiary')
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, related_name='transaction')

    def __str__(self):
        return self.user
