from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('meus_livros/', views.meus_livros, name='meus_livros'),
    path('livro_info/<int:id>', views.livro_info, name='livro_info' ),
    path('cadastrar_livro', views.cadastrar_livro, name= 'cadastrar_livro'),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('solicitar_emprestimo', views.solicitar_emprestimo, name='solicitar_emprestimo'),
    path('area_aluno', views.area_aluno, name='area_aluno'),
    path('solicitações', views.solicitações, name='solicitações'),
    path('excluir_livro/<str:id>', views.excluir_livro, name='excluir_livro'),
    path('reservar<str:id>', views.reservar, name='reservar'),
    path('devolução<str:id>', views.devolução, name='devolução')

]
