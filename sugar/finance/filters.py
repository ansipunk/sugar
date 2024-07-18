from django_filters import rest_framework as filters

from . import models


class WalletFilter(filters.FilterSet):
    min_balance = filters.NumberFilter(field_name="balance", lookup_expr="gte")
    max_balance = filters.NumberFilter(field_name="balance", lookup_expr="lte")
    balance = filters.NumberFilter(field_name="balance", lookup_expr="exact")
    label = filters.CharFilter(field_name="label", lookup_expr="exact")

    class Meta:
        model = models.Wallet
        fields = ("min_balance", "max_balance", "balance", "label")


class TransactionFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr="lte")
    amount = filters.NumberFilter(field_name="amount", lookup_expr="exact")
    wallet = filters.UUIDFilter(field_name="wallet", lookup_expr="exact")
    txid = filters.CharFilter(field_name="txid", lookup_expr="exact")

    class Meta:
        model = models.Transaction
        fields = ("min_amount", "max_amount", "amount", "wallet", "txid")
