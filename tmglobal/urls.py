from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from tmglobal.views import home, hcorp
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("", hlogin, name="hlogin"),  # Home Login
    path("", home, name="home"),  # Home Login
    # path("", TemplateView.as_view(template_name="registration/home.html"), name="home"),
    path("hcorp/", hcorp, name="hcorp"),  # Home Corporativo
]
