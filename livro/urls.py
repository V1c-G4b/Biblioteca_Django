from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('meus_livros/', views.meus_livros, name='meus_livros'),
    path('livro_info/<int:id>', views.livro_info, name='livro_info' ),
    path('cadastrar_livro', views.cadastrar_livro, name= 'cadastrar_livro'),
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('emprestar_livro', views.emprestar_livro, name='emprestar_livro')

]
