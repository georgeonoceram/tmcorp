from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path(
        "htmrat/", views.RatListViewBase.as_view(), name="htmrat"
    ),  # Lista os Relatórios de At. Técnico
    path(
        "ratview/<pk>",
        views.RatViewBase.as_view(),
        name="ratview",
    ),  # Visualizar Cadastro do Relatório de At. Técnico
    path(
        "ratcreate/", views.RatCreatetBase.as_view(), name="ratcreate"
    ),  # Inserir Cadastro de RAT
    path(
        "ratupdate/<pk>",
        views.RatUpdatetBase.as_view(),
        name="ratupdate",
    ),  # Alterar RAT
    path(
        "ratdelete/<pk>",
        views.RatDeletetBase.as_view(),
        name="ratdelete",
    ),  # Delete Cadastro RAT
]
