from django.db import models
from datetime import date, datetime, timedelta
from usuarios.models import Usuario
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.nome



class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    data_cadastro = models.DateField(default = date.today)
    estoque = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to='foto_livro', null=True, blank=True)


    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    today = datetime.today()

    nome_alugado = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING,blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete = models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(default= datetime.today())
    data_devolução = models.DateTimeField(default = today + timedelta(days=7) )
    solicitado = models.BooleanField(default= False)
    reservado = models.BooleanField(default=False)
    devolvido = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.nome_alugado} | {self.livro}'