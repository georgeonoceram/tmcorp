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

    probl_rat = models.TextField(
        verbose_name="Desc. do Problema Apresentado",
        db_comment="Descrição do Problema Apresentado",
        max_length=300,
    )

    desc_rat = models.TextField(
        verbose_name="Descrição do Atendimento",
        db_comment="Descrição do Atendimento do RAT",
        max_length=300,
    )

    conclusao_rat = models.TextField(
        verbose_name="Descrição da Conclusão Problema",
        db_comment="Descrição da Conclusão Problema do RAT",
        max_length=300,
    )

    desc_pecas_rat = models.TextField(
        verbose_name="Descrição das Peças do RAT",
        db_comment="Descrição das peças utilizadas no atendimento do RAT",
        max_length=300,
    )

    hr_ini_rat = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Hora Inicial do RAT",
        db_comment="Hora Inicial do RAT",
    )

    hr_fim_rat = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Hora Final do RAT",
        db_comment="Hora Final do RAT",
    )

    vl_atend_rat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor do atendimento",
        db_comment="Valor do atendimento do RAT",
    )

    vl_pecas_rat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor das peças",
        db_comment="Valor das peças do RAT",
    )


# cliente
# telefone cliente
# contato cliente
# endereço cliente
# solicitante
# técnico responsável
