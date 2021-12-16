from django.shortcuts import render

def mis_favoritos(request):
    template_name = "favoritos/mis_favoritos.html"
    context = {}
    return render(request, template_name, context)
