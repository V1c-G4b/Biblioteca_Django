from django import forms
from .models import Livros, Categoria,Emprestimo


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"

class CadastroCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['descricao'].widget = forms.Textarea(attrs={'cols':'35', 'rows':'5'})

# class EmprestimoLivro(forms.ModelForm):
#     class Meta:
#         model = Emprestimo
#         fields = "__all__"
#         exclude = ['solicitado', 'reservado' 'devolvido', 'data_emprestimo' , 'data_devolução']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['livro'].widget = forms.HiddenInput()
#         self.fields['nome_alugado'] = forms.HiddenInput()