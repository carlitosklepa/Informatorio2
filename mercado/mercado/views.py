from django.shortcuts import render
from productos.models import Producto

def inicio(request):
    productos = Producto.objects.all()

    usuario = {
        "nombre": "Carlos",
        "apellido": "Klepacek"
    }

    context = {
        "usuario": usuario,
        "productos": productos
    }
    return render(request, "inicio.html", context)

def login(request):
    
    return render(request, "login.html")
