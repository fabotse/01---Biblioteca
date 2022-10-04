from email.policy import default
from django.db import models
from datetime import date

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    nome_emprestado = models.CharField(max_length=200, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateTimeField(blank=True, null=True)