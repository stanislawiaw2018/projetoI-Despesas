from django.db import models


# Create your models here.
from django.utils import timezone


class Despesa(models.Model):
    CARTAO = 'CA'
    BOLETO = 'BO'
    CREDIARIO = 'CRE'
    DINHEIRO = 'DI'
    pagamento = (
        (CARTAO, 'cartao'),
        (BOLETO, 'boleto'),
        (CREDIARIO, 'crediario'),
        (DINHEIRO, 'dinheiro'),
    )
    data_criacao = models.DateTimeField(default=timezone.now)
    tipo_despesa = models.CharField(max_length=50)
    forma_pagamento = models.CharField(
        max_length =3,
        choices = pagamento,
        default = CARTAO,
    )
    descricao = models.TextField()
    vencimento = models.DateField(null=True, blank=True)
    quitado = models.BooleanField(default=True)



def __str__(self):
    return self.despesa
