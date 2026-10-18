from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'password': 'Contraseña'
        }
        widgets = {
            'password': forms.PasswordInput()
        }