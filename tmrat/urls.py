from django.urls import path

from tmrat.views import home

urlpatterns = [
    path('', home),  # Home
]