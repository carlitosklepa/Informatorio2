from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre del Producto", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre del producto"}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    # attrs={'cols':80, 'rows': 20} - DENTRO DEL PARENTESIS DEL TEXTAREA()

    class Meta:
        model = Producto
        fields = ["nombre", "precio", "categorias", "descripcion", "imagen", "estado"]
