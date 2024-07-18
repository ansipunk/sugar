from django.core import exceptions as django_exceptions
from django_filters import rest_framework as django_filters
from rest_framework import exceptions as rest_exceptions
from rest_framework import filters as rest_filters
from rest_framework import viewsets

from . import filters
from . import models
from . import serializers


class WalletViewSet(viewsets.ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer
    filter_backends = (django_filters.DjangoFilterBackend, rest_filters.OrderingFilter)
    filterset_class = filters.WalletFilter
    ordering_fields = ("label", "balance")

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    filter_backends = (django_filters.DjangoFilterBackend, rest_filters.OrderingFilter)
    filterset_class = filters.TransactionFilter
    ordering_fields = ("amount",)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except django_exceptions.ValidationError as e:
            raise rest_exceptions.ValidationError(detail=str(e))

    def update(self, request, *args, **kwargs):
        raise rest_exceptions.MethodNotAllowed(
            "PUT",
            detail="Transactions cannot be updated",
        )

    def delete(self, request, *args, **kwargs):
        raise rest_exceptions.MethodNotAllowed(
            "DELETE",
            detail="Transactions cannot be deleted",
        )
