from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Cards(models.Model):
    card_name = models.CharField(max_length=255, blank=False, null=False)
    card_number = models.IntegerField()
    expiry_date = models.DateField()
    cvv = models.IntegerField()


class Next_Of_Kin(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    relationship = models.CharField(max_length=255, blank=False, null=False)
    bvn = models.IntegerField()


class User(AbstractUser):
    email = models.EmailField(unique=True)
    next_0f_kin = models.ForeignKey(Next_Of_Kin, on_delete=models.CASCADE, related_name='next_of_kin')
    home_address = models.CharField(max_length=255)
    nin = models.IntegerField(blank=False, null=False)


class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    card = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name='card')
