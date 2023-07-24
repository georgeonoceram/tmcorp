from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
     choices_cargo = (('A', 'Analista'), 
                      ('D', 'Diretor'))
     noccargo = models.CharField(max_length=1, choices=choices_cargo)