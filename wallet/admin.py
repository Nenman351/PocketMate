from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from wallet.models import Wallet, User


# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'account']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'home_address', 'nin']
