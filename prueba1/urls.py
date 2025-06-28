"""
URL configuration for prueba1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluye las rutas de cada app
    path('api/Producto/', include('Producto.urls')),
    path('api/Inventario/', include('Inventario.urls')),
    path('api/usuario/', include('usuario.urls')),
    path('api/calendario/', include('calendario.urls')),
    path('api/iniciosesion/', include('iniciosesion.urls')),
    path('api/conferencias/', include('conferencias.url')),
]

