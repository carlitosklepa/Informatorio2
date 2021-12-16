from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('detalle/<int:pk>/', views.Detalle.as_view(), name="detalle"),

    #Admin
    path('admin/listar/', views.ListarAdmin.as_view(), name="admin_listar"),
    path('admin/nuevo/', views.NuevoAdmin.as_view(), name="admin_nuevo"),
    path('admin/editar/<int:pk>/', views.EditarAdmin.as_view(), name="admin_editar"),

    path('MisProductos', views.MisProductos.as_view(), name="mis_productos")
]
