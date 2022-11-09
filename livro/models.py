from django.db import models
from datetime import date, datetime, timedelta
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length = 60)
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    
    def __str__(self):
        return self.nome



class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    data_cadastro = models.DateField(default = date.today)
    alugado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)


    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Otimo')
    )
    today = datetime.today()

    nome_alugado = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING,blank = True, null = True)
    data_emprestimo = models.DateTimeField(default= datetime.today())
    data_devolução = models.DateTimeField(default = today + timedelta(days=2) )
    livro = models.ForeignKey(Livros, on_delete = models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices = choices, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.nome_alugado} | {self.livro}'