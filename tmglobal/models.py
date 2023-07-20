from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class NocUsers(AbstractBaseUser):
     choices_cargo = (('A', 'Analista'), 
                      ('D', 'Diretor'))
     noc_cargo = models.CharField(max_length=1, choices=choices_cargo)