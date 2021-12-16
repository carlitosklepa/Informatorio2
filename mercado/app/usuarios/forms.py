from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario

class UsuarioForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre de usuario"}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su nombre"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su apellido"}))
    #password = forms.CharField(widget=forms.PasswordInput())
    #password2 = forms.CharField(widget=forms.PasswordInput())
    # HACER LO MISMO CON TODOS LOS CAMPOS DEL FORMULARIO

    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "dni"]
'''
        # PARA HACER CONTROLES EN LOS CAMPOS:
    def clean_username(self):
        username = self.cleaned_data["username"]
        if 123 in username:
            raise ValidationError("Mensaje de por qué se considera un error")
        return username
'''
