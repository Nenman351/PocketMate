from django.urls import path, include
from pycparser.c_ast import Default
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('wallet', views.WalletCreate)

urlpatterns = [
    path('', include(router.urls)),
]
