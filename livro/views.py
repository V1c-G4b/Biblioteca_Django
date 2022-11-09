from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Categoria, Livros, Emprestimo
from .forms import CadastroLivro, CadastroCategoria,EmprestimoLivro

from usuarios.models import Usuario
# Create your views here.

def home(request):
    if request.session.get('usuario'):    
        return render(request, 'home.html', {'usuario_logado':request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')

def meus_livros(request):
    if request.session.get('usuario'):    
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        status = request.GET.get('status')
        form = CadastroLivro()
        form_categoria = CadastroCategoria()
        form_categoria.fields['usuario'].initial = request.session['usuario']
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)


        # livros_emprestados = Livros.objects.filter(usuario)

        return render(request, 'meus_livros.html', {'livros': livros,
                                                    'usuario_logado':request.session.get('usuario'),
                                                    'ver_livros':request.session.get('usuario'),
                                                    'form':form,
                                                    'form_categoria' : form_categoria,
                                                    'status':status})
    else:
        return redirect('/auth/login/?status=2')

def livro_info(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        status = request.GET.get('status')


        if request.session.get('usuario') == livros.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro = livros)
            form = CadastroLivro()
            form_categoria = CadastroCategoria()
            form_emprestimo = EmprestimoLivro()
            form_categoria.fields['usuario'].initial = request.session['usuario']
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)


            return render(request, 'livro_info.html',{'livro' : livros, 
                                                      'categoria_livro': categoria_livro, 
                                                      'emprestimos': emprestimos, 
                                                      'usuario_logado':request.session.get('usuario'),
                                                      'form':form,
                                                      'form_categoria':form_categoria,
                                                      'form_emprestimo':form_emprestimo,
                                                      'ver_livros':request.session.get('usuario'),
                                                      'status':status,
                                                      'id_livro':id})
        
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


def emprestar_livro(request):
    if request.method == 'POST':
        form_emprestimo = EmprestimoLivro(request.POST)
        if form_emprestimo.is_valid():
            form_emprestimo.save()

            
            return redirect('/livro/meus_livros')
        else:
            return redirect('/livro/meus_livros?status=1')

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/meus_livros')