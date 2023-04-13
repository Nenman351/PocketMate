from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from wallet.models import Wallet


class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'account']


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
