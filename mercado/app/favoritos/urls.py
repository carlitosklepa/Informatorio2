from django.urls import path
from . import views

app_name = "davoritos"

urlpatterns = [
    path('MisFavoritos/', views.mis_favoritos, name="mis_favoritos"),

]

'''
ESTO TIENE QUE IR EN BASE.HTML PARA EL BOTÓN DE "MIS FAVORITOS"
<li class="nav-item">
<a class="nav-link" href="{% url 'favoritos:mis_favoritos' %}">Mis Favoritos</a>
'''
