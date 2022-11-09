from django.contrib import admin
from .models import Livros, Categoria, Emprestimo


# Register your models here.
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimo)