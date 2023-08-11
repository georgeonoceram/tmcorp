from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path(
        "htmrat/", views.ForneceListViewBase.as_view(), name="htmrat"
    ),  # Relatório de At. Técnico
]
