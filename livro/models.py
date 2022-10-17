from email.policy import default
from django.db import models
from datetime import date
from usuarios.models import Usuario


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
   
    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    nome_emprestado_anonimo = models.CharField(max_length=200, blank=True, null=True)
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)