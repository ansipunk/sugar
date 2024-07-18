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

        self.assertEqual(wallet.label, "Test Wallet")
        self.assertEqual(wallet.balance, 0)


class TransactionModelTests(test.TestCase):
    def setUp(self):
        self.wallet = models.Wallet.objects.create(
            id=uuid.uuid4(),
            label="Test Wallet",
        )

    def test_transaction_creation(self):
        self.assertEqual(self.wallet.balance, 0)

        models.Transaction(
            wallet=self.wallet, txid="txid", amount=100,
        ).save()

        self.assertEqual(self.wallet.balance, 100)

        models.Transaction(
            wallet=self.wallet, txid="txid", amount=-50,
        ).save()

        self.assertEqual(self.wallet.balance, 50)

    def test_transaction_illegal(self):
        self.assertEqual(self.wallet.balance, 0)

        with self.assertRaises(exceptions.ValidationError):
            models.Transaction(
                wallet=self.wallet, txid="txid", amount=-100,
            ).save()
