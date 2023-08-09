from django.contrib import admin
from tmrat.models.rat import RelAtTec


@admin.register(RelAtTec)
class AdmRat(admin.ModelAdmin):
    ...
