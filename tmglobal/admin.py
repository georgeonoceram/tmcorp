from django.contrib import admin
from tmglobal.models.usuarios import Users
from django.contrib.auth import admin as noc_admin_auth_django
from tmglobal.forms.frm_admin import UserChangeForms, UserCreationForms


@admin.register(Users)
class UsersAdmin(noc_admin_auth_django.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    model = UserChangeForms
    fieldsets = noc_admin_auth_django.UserAdmin.fieldsets + (
        ("Tecmed", {"fields": ["usr_empresa", "usr_filial", "usr_cargo"]}),
    )
