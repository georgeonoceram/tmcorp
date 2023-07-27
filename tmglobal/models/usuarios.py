from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    choices_cargo = (("A", "Analista"), ("D", "Diretor"))
    choices_empresa = (("01", "Tecmed Matriz"), ("02", "Tecmed Filial US"))
    noc_cargo = models.CharField(max_length=1, choices=choices_cargo)
    noc_empresa = models.CharField(max_length=50, choices=choices_empresa, default="")
