from django.urls import path
from tmglobal.views import home

urlpatterns = [
     path('', home),  # Home
]