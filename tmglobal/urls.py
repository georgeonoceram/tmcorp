from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from tmglobal.views.vw_tmglobal import home, hcorp, vw_corpcli, vw_corpfor
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),  # Home Login
    path("hcorp/", hcorp, name="hcorp"),  # Home Corporativo
    path("corpcli/", vw_corpcli, name="corpcli"),  # Cadastro de Clientes
    path("corpfor/", vw_corpfor, name="corpfor"),  # Cadastro de Fornecedores
]
