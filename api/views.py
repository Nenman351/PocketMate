from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import WalletCreateSerializer
from wallet.models import Wallet


# Create your views here.

class WalletCreate(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletCreateSerializer
