from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")),  # Auth routes - login / register
    path("", include("apps.main.urls")),          # UI Kits Html files
    path('trade/', include("apps.trade.urls")),            # Trade app
]
