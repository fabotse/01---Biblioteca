from email.policy import default
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    #Devido a quantidade de Hash
    senha = models.CharField(max_length = 64)
    ativo = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.nome