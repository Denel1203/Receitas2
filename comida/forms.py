from django.forms import ModelForm

from .models import Comentario, Receitas


# Create the form class.
class ReceitasForm(ModelForm):
    class Meta:
        model = Receitas
        fields = ['Name', 'Nome_Receita', 'Ingredientes', 'Instrucoes', 'Notas']
        
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['Nome', 'comentario']