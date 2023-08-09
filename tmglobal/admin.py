from django.contrib import admin
from tmglobal.models.usuarios import Users
from django.contrib.auth import admin as noc_admin_auth_django
from tmglobal.forms.frm_admin import UserChangeForms, UserCreationForms
from tmglobal.models.corporativo import Clientes, Fornecedores, Empresas


@admin.register(Users)
class UsersAdmin(noc_admin_auth_django.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    model = UserChangeForms
    fieldsets = noc_admin_auth_django.UserAdmin.fieldsets + (
        ("Tecmed", {"fields": ["usr_empresa", "usr_filial", "usr_cargo"]}),
    )


@admin.register(Clientes)
class AdmCliente(admin.ModelAdmin):
    ...


@admin.register(Fornecedores)
class AdmCliente(admin.ModelAdmin):
    ...


@admin.register(Empresas)
class AdmCliente(admin.ModelAdmin):
    ...
