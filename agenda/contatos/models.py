from django.db import models
from django.utils import timezone
"""
CONTATOS
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

CATEGORIA
nome: STR * (obrigatório)

"""


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    objects = None
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)  # Para dizer que é opcional
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)  # Para dizer que é opcional
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome



