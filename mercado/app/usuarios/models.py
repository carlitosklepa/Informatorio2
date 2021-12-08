from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)
    # foto = models.ImageField()

    class Meta:
        db_table="usuarios"
