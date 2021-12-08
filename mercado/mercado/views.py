from django.shortcuts import render
from app.productos.models import Producto

def inicio(request):
    context = {
        "productos": Producto.objects.all()
    }
    return render(request, "inicio.html", context)

def login(request):
    print("=============")
    print(request.POST.get("username", None))
    return render(request, "login.html")
