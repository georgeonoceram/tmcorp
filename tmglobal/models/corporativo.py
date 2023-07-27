from django.db import models


class uf(models.Model):
    UF_BR_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AM", "Amazonas"),
        ("AP", "Amapa"),
        ("BA", "Bahia"),
        ("CE", "Ceara"),
        ("DF", "Distrito federal"),
        ("ES", "Espirito santo"),
        ("EX", "Estrangeiro"),
        ("GO", "Goias"),
        ("MA", "Maranhao"),
        ("MG", "Minas gerais"),
        ("MS", "Mato grosso do sul"),
        ("MT", "Mato grosso"),
        ("PA", "Para"),
        ("PB", "Paraiba"),
        ("PE", "Pernambuco"),
        ("PI", "Piaui"),
        ("PR", "Parana"),
        ("RJ", "Rio de janeiro"),
        ("RN", "Rio grande do norte"),
        ("RO", "Rondonia"),
        ("RR", "Roraima"),
        ("RS", "Rio grande do sul"),
        ("SC", "Santa catarina"),
        ("SE", "Sergipe"),
        ("SP", "Sao paulo"),
        ("TO", "Tocantins"),
    ]


class empresas(models.Model):
    empresas_pk = models.IntegerField(primary_key=True)
    cod_empresa = models.CharField(
        verbose_name="Cod.Empresa",
        db_comment="Código da empresa que será relalcionado com todo sistema",
        max_length=2,
    )
    cod_filial = models.CharField(
        verbose_name="Cod.Filial",
        db_comment="Código da filial que será relalcionado com todo sistema",
        max_length=2,
    )
    nome_empresa = models.CharField(
        verbose_name="Nome Empresa",
        db_comment="Nome da empresa",
        max_length=40,
    )
    nome_filial = models.CharField(
        verbose_name="Nome Filial",
        db_comment="Nome da Filial",
        max_length=40,
    )
    nome_comercial = models.CharField(
        verbose_name="Nome Comercial",
        db_comment="Nome da Comercial",
        max_length=60,
    )

    # telefone
    # cnpj
    # endereco
    # end_complemento
    # end_bairro
    # end_cidade
    # end_cep
    end_uf = (
        models.CharField(
            verbose_name="Estado UF",
            db_comment="Sigla e descrição do estado brasileiro - Estrangeiro: EX",
            max_length=2,
            choices=uf.UF_BR_CHOICES,
        ),
    )
    # cnae
    # lic_licenca
    # lic_chave
    # lic_checksum
    # lic_validade

    class Meta:
        indexes = [
            models.Index(fields=["cod_empresa", "cod_filial"]),
        ]
