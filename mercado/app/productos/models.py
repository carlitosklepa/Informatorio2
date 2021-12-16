from django.db import models

from app.usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        db_table="categorias"

    def __str__(self):
        return self.nombre

ESTADOS_CHOICES = (
    (1, "ACTIVO"),
    (2, "INACTIVO"),
    (3, "SIN STOCK")
)

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(default="")
    precio = models.DecimalField(max_digits=9, decimal_places=2)

    categorias = models.ManyToManyField(Categoria)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    imagen = models.ImageField(upload_to="productos", null=True)

    estado = models.IntegerField(choices=ESTADOS_CHOICES, default=1)

    class Meta:
        db_table="productos"

    def __str__(self):
        return self.nombre
