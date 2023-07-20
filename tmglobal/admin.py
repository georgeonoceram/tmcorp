import imp
from django.contrib import admin
from .models import NocUsers
from django.contrib.auth import admin as noc_admin_auth_django
from .forms import NocChangeForms, NocCreationForms

@admin.register(NocUsers)
class NocUserAdmin(noc_admin_auth_django.UserAdmin):
     form = NocChangeForms
     add_form = NocCreationForms
     model = NocUsers