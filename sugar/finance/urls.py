from django import urls
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r"wallets", views.WalletViewSet)
router.register(r"transactions", views.TransactionViewSet)

urlpatterns = [
    urls.path("", urls.include(router.urls)),
]
