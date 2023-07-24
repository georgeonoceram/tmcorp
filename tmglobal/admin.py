from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as noc_admin_auth_django
from .forms import UserChangeForms, UserCreationForms

@admin.register(Users)
class UsersAdmin(noc_admin_auth_django.UserAdmin):
     form = UserChangeForms
     add_form = UserCreationForms
     model = UserChangeForms
     fieldsets = noc_admin_auth_django.UserAdmin.fieldsets + ((None, {"fields": ["noccargo"]}),)