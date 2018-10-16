from django import forms
from .models import Post
from .models import Pessoal

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title', 'text')

class PostPessoal(forms.ModelForm):

    class Meta:
        model = Pessoal
        fields = ('nome', 'sobrenome' , 'idade' , 'datadenacimento', 'endereco', 'sexo', 'cor', )


