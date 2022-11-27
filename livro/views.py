import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Categoria, Livros, Emprestimo
from .forms import CadastroLivro, CadastroCategoria

from usuarios.models import Usuario
# Create your views here.


def home(request):
    if request.session.get('usuario'):

        usuario = Usuario.objects.get(id=request.session['usuario'])

        return render(request, 'home.html', {'usuario_logado': request.session.get('usuario'),
                                             'usuario': usuario})
    else:
        return redirect('/auth/login/?status=2')


def meus_livros(request):
    if request.session.get('usuario'):

        filtro_livro = request.GET.get('Livro')
        filtro_autor = request.GET.get('Autor')
        filtro_categoria = request.GET.get('Gênero')
        livros = Livros.objects.all()
        categoria = Categoria.objects.all()
        if filtro_livro:
            livros = Livros.objects.filter(nome__icontains=filtro_livro)
        if filtro_autor:
            livros = Livros.objects.filter(autor__icontains=filtro_autor)
        if filtro_categoria:
            livros = Livros.objects.filter(categoria=filtro_categoria)

        usuario = Usuario.objects.get(id=request.session['usuario'])
        status = request.GET.get('status')

        form = CadastroLivro()
        form_categoria = CadastroCategoria()

        return render(request, 'meus_livros.html', {'livros': livros,
                                                    'categoria': categoria,
                                                    'usuario_logado': request.session.get('usuario'),
                                                    'ver_livros': request.session.get('usuario'),
                                                    'form': form,
                                                    'form_categoria': form_categoria,
                                                    'status': status})
    else:
        return redirect('/auth/login/?status=2')


def livro_info(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        status = request.GET.get('status')

        if request.session.get('usuario'):
            emprestimos = Emprestimo.objects.filter(livro=livros)
            # form_emprestimo = EmprestimoLivro()

            return render(request, 'livro_info.html', {'livro': livros,
                                                       'emprestimos': emprestimos,
                                                       'usuario_logado': request.session.get('usuario'),
                                                       'ver_livros': request.session.get('usuario'),
                                                       'status': status,
                                                       'id_livro': id})

        else:
            return HttpResponse('Este livro não é seu')
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/meus_livros')
        else:
            return redirect('/livro/meus_livros?status=1')


def cadastrar_categoria(request):
    if request.method == 'POST':
        form_categoria = CadastroCategoria(request.POST)

        if form_categoria.is_valid():
            form_categoria.save()
            return redirect('/livro/meus_livros')
        else:
            return redirect('/livro/meus_livros?status=1')


def solicitar_emprestimo(request):
    livro_id = request.POST.get('livro_id')
    livro = Livros.objects.get(id=livro_id)
    usuario = Usuario.objects.get(id=request.session['usuario'])

    emprestimo = Emprestimo(
        livro=livro,
        nome_alugado=usuario,
        solicitado=True
    )
    emprestimo.save()
    return redirect('/livro/meus_livros/')


def confirmar_reserva(request):
    pass




def area_aluno(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        if usuario.aluno:
            emprestimo = Emprestimo.objects.filter(nome_alugado=usuario)

            return render(request, 'area_aluno.html', {'usuario_logado': request.session.get('usuario'),
                                                       'usuario': usuario,
                                                       'emprestimo': emprestimo})
        else:
            return redirect('/livro/home')
    else:
        return redirect('/auth/login/?status=2')


def solicitações(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        if not usuario.aluno:
            emprestimo = Emprestimo.objects.all()
            return render(request, 'solicitações.html', {'usuario_logado': request.session.get('usuario'),
                                                         'usuario': usuario,
                                                         'emprestimo': emprestimo})
        else:
            return redirect('/livro/home')


def reservar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.solicitado = False
    emprestimo.reservado = True
    emprestimo.save()
    return redirect('/livro/solicitações')


def devolução(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.reservado = False
    emprestimo.devolvido = True
    emprestimo.save()
    return redirect('/livro/solicitações')

def excluir_livro(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    return redirect('/livro/solicitações')