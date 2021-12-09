from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('detalle/', views.detalle, name="detalle")


]
