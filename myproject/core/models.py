from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100, default="")
    # outros campos específicos do modelo Usuario

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # outros campos específicos do modelo Empréstimo

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # outros campos específicos do modelo Reserva

class Equipamento(models.Model):
    nome = models.CharField(max_length=100, default="")
    # outros campos específicos do modelo Equipamento
