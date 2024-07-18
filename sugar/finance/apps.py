from django import apps


class FinanceConfig(apps.AppConfig):
    default_auto_field = "django.db.models.UUIDField"
    name = "sugar.finance"
