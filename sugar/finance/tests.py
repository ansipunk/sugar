import contextlib
import uuid

from django import test
from django.core import exceptions

from . import models


class WalletModelTests(test.TestCase):
    def setUp(self):
        self.wallet = models.Wallet.objects.create(
            id=uuid.uuid4(),
            label="Test Wallet",
        )

    def test_wallet_creation(self):
        """Test that a Wallet object is created successfully."""
        wallet = models.Wallet.objects.get(id=self.wallet.id)
        assert wallet.label == "Test Wallet"
        assert wallet.balance == 0


class TransactionModelTests(test.TestCase):
    def setUp(self):
        self.wallet = models.Wallet.objects.create(
            id=uuid.uuid4(),
            label="Test Wallet",
        )

    def test_transaction_creation(self):
        assert self.wallet.balance == 0

        models.Transaction(
            wallet=self.wallet, txid="txid", amount=100,
        ).save()

        assert self.wallet.balance == 100

    def test_transaction_negative(self):
        assert self.wallet.balance == 0

        models.Transaction(
            wallet=self.wallet, txid="txid", amount=100,
        ).save()
        models.Transaction(
            wallet=self.wallet, txid="txid", amount=-50,
        ).save()

        assert self.wallet.balance == 50

    def test_transaction_illegal(self):
        assert self.wallet.balance == 0

        with contextlib.suppress(exceptions.ValidationError):
            models.Transaction(
                wallet=self.wallet, txid="txid", amount=-100,
            ).save()
