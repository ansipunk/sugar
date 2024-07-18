from rest_framework import serializers

from . import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ("id", "wallet", "txid", "amount")


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    balance = serializers.DecimalField(max_digits=18, decimal_places=6, read_only=True)

    class Meta:
        model = models.Wallet
        fields = ("id", "label", "balance", "transactions")
        read_only_fields = ("balance",)

    def update(self, instance, validated_data):
        instance.label = validated_data.get("label", instance.label)
        instance.save()
        return instance
