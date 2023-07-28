from django.db import models
from .tmrat_choices import Noc_RAT_Choices


class RelAtTec(models.Model):
    rat_pk = models.IntegerField(primary_key=True)
    tp_rat = models.CharField(
        verbose_name="Tipo RAT",
        db_comment="Tipo do Relatório de Atendimento Técnico",
        max_length=1,
        choices=Noc_RAT_Choices.TP_RAT_CHOICES,
    )

    dt_rat = models.DateField(
        verbose_name="Data RAT",
        db_comment="Data do Relatório de Atendimento Técnico",
    )


# hora inicial
# hora final
# cliente
# telefone cliente
# contato cliente
# endereço cliente
# solicitante
# técnico responsável
# problema apresentado
# descrição do atendimento
# conclusão do atendimento
# descrição de peças usadas
# Vl Chamado
# Vl Peças
# Vl Total
