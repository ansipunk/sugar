import uuid

from django.core import exceptions
from django.db import models
from django.db import transaction


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=127, blank=False, null=False)
    balance = models.DecimalField(
        max_digits=18,
        decimal_places=6,
        editable=False,
        default=0,
        null=False,
    )

    def __str__(self):
        return f"Wallet {self.label}: {self.balance}"

    class Meta:
        indexes = (
            models.Index(fields=["label"]),
            models.Index(fields=["balance"]),
        )


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(
        Wallet,
        related_name="transactions",
        on_delete=models.CASCADE,
    )
    txid = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    amount = models.DecimalField(
        max_digits=18,
        decimal_places=6,
        null=False,
    )

    def clean(self):
        if self.amount < 0:
            projected_balance = self.wallet.balance + self.amount

            if projected_balance < 0:
                raise exceptions.ValidationError("Insufficient funds")

    def save(self, *args, **kwargs):
        # We do this within a transaction to ensure that parallel requests
        # to the same wallet do not engage in a race condition.
        with transaction.atomic():
            self.clean()

            self.wallet.balance += self.amount
            self.wallet.save()

            super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.txid}: {self.wallet.label} - {self.amount}"

    class Meta:
        indexes = (
            models.Index(fields=["wallet"]),
            models.Index(fields=["txid"]),
            models.Index(fields=["amount"]),
        )
