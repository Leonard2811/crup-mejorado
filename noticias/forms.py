from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del artículo',
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el contenido del artículo...',
                'rows': 12,
            }),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
        }
