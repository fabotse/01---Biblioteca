from email.policy import default
from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)


class Emprestimo(models.Model):
    nome_emprestado = models.DateTimeField()
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.DateTimeField()