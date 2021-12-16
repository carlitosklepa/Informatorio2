from django.shortcuts import render
from django.views.generic.base import TemplateView
from app.productos.models import Producto

from django.views.generic import ListView

class Inicio(ListView):
    template_name="inicio.html"
    model = Producto
    context_object_name="productos"

    def get_queryset(self):
        return Producto.objects.filter(estado__in=[1, 3])




'''
# INICIO BASADO EN CLASE

class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context



# INICIO BASADO EN FUNCIÓN

def inicio(request):
    context = {
        "productos": Producto.objects.all()
    }
    return render(request, "inicio.html", context)
'''
