from django.db import models


class Noc_RAT_Choices(models.Model):
    TP_RAT_CHOICES = [
        ("A", "Avulso"),
        ("C", "Contrato"),
        ("G", "Garantia"),
    ]
