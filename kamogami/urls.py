"""kamogami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include

from .views import IndexView, AboutView

from reservas import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index_class/", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    # TODO: Cambiar a class based views
    path("admin/", admin.site.urls),
    path("inicio/", views.inicio),
    path("contacto/", views.contacto),
    path("agendar-hora/", views.agendar),
    # deprectaed
    path("miperfil/", views.mi_perfil),
    path("recuperar/", views.recuperar),
    path("", views.inicio),
    # Desde usuarios
    path("", include("usuarios.urls")),
]
