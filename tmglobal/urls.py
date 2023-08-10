from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from tmglobal.views.vw_tmglobal import hcorp, vw_corpfor, home, test
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),  # Home Login
    path("hcorp/", hcorp, name="hcorp"),  # Home Corporativo
    path(
        "glbclient/", views.ClientListViewBase.as_view(), name="glbclient"
    ),  # Cadastro de Clientes
    path("corpfor/", vw_corpfor, name="corpfor"),  # Cadastro de Fornecedores
    path("test/", test, name="test"),  # Home Login
]
