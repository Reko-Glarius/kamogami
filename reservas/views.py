from django.shortcuts import render
from django.views.generic import ListView
from django.template import Template, Context, context
from django.http import HttpResponse
from pathlib import Path
from reservas.models import servicio
import os
import logging

logger = logging.getLogger(__name__)

# Confused fubuki
BASE_DIR = Path(__file__).resolve().parent


class ServicioView(ListView):
    model = servicio
    template_name = "reservas/servicio-list.html"


# TODO: mover y refactorizar


def inicio(request):
    doc_externo = open(os.path.join(BASE_DIR, "templates/inicio/inicio.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    info = servicio.objects.all()
    dcto = {
        "card1": info[0].description,
        "card1_titulo": info[0].name,
        "card2": info[1].description,
        "card2_titulo": info[1].name,
        "card3": info[2].description,
        "card3_titulo": info[2].name,
        "card4": info[3].description,
        "card4_titulo": info[3].name,
    }
    ctx = Context(dcto)
    documento = plt.render(ctx)
    return HttpResponse(documento)


def contacto(request):
    doc_externo = open(os.path.join(BASE_DIR, "templates/contacto/contacto.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    dcto = {}
    ctx = Context(dcto)
    documento = plt.render(ctx)
    return HttpResponse(documento)


def agendar(request):
    # remove
    doc_externo = open(os.path.join(BASE_DIR, "templates/agendarHora/agendar.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    dcto = {}
    ctx = Context(dcto)
    documento = plt.render(ctx)
    return HttpResponse(documento)


def recuperar(request):
    doc_externo = open(os.path.join(BASE_DIR, "templates/recuperar/recuperar.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    dcto = {}
    ctx = Context(dcto)
    documento = plt.render(ctx)
    return HttpResponse(documento)


def mi_perfil(request):
    # remove
    doc_externo = open(os.path.join(BASE_DIR, "templates/miperfil/mi_perfil.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    dcto = {}
    ctx = Context(dcto)
    documento = plt.render(ctx)
    return HttpResponse(documento)
