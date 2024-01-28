# En gestorpass/forms.py
from django import forms
from .models import PasswordEntry

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['title', 'username', 'password', 'url', 'notes']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'your-css-class'}),
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'url': forms.URLInput(),
            'notes': forms.Textarea(),
        }

        labels = {
            'title': 'Título',
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
            'url': 'URL',
            'notes': 'Notas',
        }
