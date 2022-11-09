from django import forms
from .models import Livros, Categoria,Emprestimo


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()


class CadastroCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()
        self.fields['descricao'].widget = forms.Textarea(attrs={'cols':'35', 'rows':'5'})

class EmprestimoLivro(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avaliacao'].widget = forms.HiddenInput()
        self.fields['livro'].queryset = Livros.objects.filter(alugado = False)