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
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('excluido', 'Excluído'),
        ('emprestado', 'Emprestado'),
        ('reparo', 'Em Reparo'),
        ('reservado', 'Reservado'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Disponível')
    foto = models.ImageField(upload_to='myproject/core/static/img/equipments/', blank=True, null=True)


    # outros campos específicos do modelo Equipamento

    def __str__(self):
        return self.nome

    def get_status_class(self):
        if self.status == 'Disponível':
            return 'badge badge-success'
        elif self.status == 'Excluído':
            return 'badge badge-danger'
        elif self.status == 'Emprestado':
            return 'badge badge-warning'
        elif self.status == 'Em Reparo':
            return 'badge badge-secondary'
        elif self.status == 'Reservado':
            return 'badge badge-primary'
        else:
            return 'badge badge-light'
