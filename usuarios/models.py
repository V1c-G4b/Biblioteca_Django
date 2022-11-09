import email
from django.db import models
from django.db.models.constraints import UniqueConstraint

class Usuario(models.Model):
    nome = models.CharField(max_length = 30)
    email = models.EmailField()
    senha = models.CharField(max_length = 64)

    def __str__(self) -> str:
        return self.nome
