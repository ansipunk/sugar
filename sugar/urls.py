from django import urls

urlpatterns = [
    urls.path("api/", urls.include("sugar.finance.urls")),
]
