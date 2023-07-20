from django import forms
from django.contrib.auth import forms
from .models import NocUsers

class Noc_Change_Forms(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = NocUsers

class Noc_Creation_Forms(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = NocUsers