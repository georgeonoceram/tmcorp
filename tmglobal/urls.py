from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from tmglobal.views import home, hcorp
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),  # Home Login
    path("hcorp/", hcorp, name="hcorp"),  # Home Corporativo
]
