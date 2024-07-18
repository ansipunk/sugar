from django.core import exceptions
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from . import models
from . import serializers


class WalletViewSet(viewsets.ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except exceptions.ValidationError as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return response.Response({"detail": "Transactions cannot be updated"}, status=405)

    def delete(self, request, *args, **kwargs):
        return response.Response({"detail": "Transactions cannot be deleted"}, status=405)
