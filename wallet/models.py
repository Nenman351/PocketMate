from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.first_name

