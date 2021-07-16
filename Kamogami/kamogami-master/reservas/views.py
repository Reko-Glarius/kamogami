from django.shortcuts import render
from django.views.generic import ListView

from reservas.models import servicio


class ServicioView(ListView):
    model = servicio
    template_name = "reservas/servicio-list.html"