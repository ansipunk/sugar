import uuid

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True
    dependencies = ()

    operations = (
        migrations.CreateModel(
            name="Wallet",
            fields=(
                ("id", models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ("label", models.CharField(max_length=127)),
                ("balance", models.DecimalField(
                    decimal_places=6,
                    default=0,
                    editable=False,
                    max_digits=18,
                )),
            ),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=(
                ("id", models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                )),
                ("txid", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=6, max_digits=18)),
                ("wallet", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="transactions",
                    to="finance.wallet",
                )),
            ),
        ),
    )
