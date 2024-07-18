from django import urls
from rest_framework import routers
from rest_framework import schemas

from . import views

router = routers.DefaultRouter()

router.register(r"wallets", views.WalletViewSet)
router.register(r"transactions", views.TransactionViewSet)

urlpatterns = [
    urls.path("", urls.include(router.urls)),
    urls.path("openapi", schemas.get_schema_view(
        title="Finance API",
        description="API for the test assignment",
        version="0.1.0a1",
    ), name="openapi-schema"),
]
