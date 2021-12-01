from django.shortcuts import render

def inicio(request):
    usuario = {
        "nombre": "Carlos",
        "apellido": "Klepacek"
    }

    context = {
        "usuario": usuario
    }
    return render(request, "inicio.html", context)

def login(request):
    return render(request, "login.html")
