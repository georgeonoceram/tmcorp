from django.contrib import admin
from django.urls import include, path
from tmglobal.views import home, hcorp

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include("tmglobal.urls")),
    path("", include("tmrat.urls")),
]
