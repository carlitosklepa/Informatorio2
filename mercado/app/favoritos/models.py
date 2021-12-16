from django.db import models
from app.usuarios.models import Usuario
from app.productos.models import Producto

class Lista(models.Model):
    suario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True)
    productos = models.ManyToManyField(Producto)

    class Meta:
        db_table="lista_favoritos"
