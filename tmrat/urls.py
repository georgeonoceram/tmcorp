from django.urls import path

from tmrat.views import htmrat

urlpatterns = [
    path("htmrat/", htmrat, name="htmrat"),  # Home RAT
]
