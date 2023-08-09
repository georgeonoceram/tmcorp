from django.urls import path

from tmrat.views.vw_tmrat import htmrat

urlpatterns = [
    path("htmrat/", htmrat, name="htmrat"),  # Home RAT
]
