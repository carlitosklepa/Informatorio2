from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.inicio, name="inicio"),
    path('', views.Inicio.as_view(), name="inicio"),

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),

    #Includes
    path('producto/', include('app.productos.urls')),
    path('usuario/', include('app.usuarios.urls')),
    path('favoritos/', include('app.favoritos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
