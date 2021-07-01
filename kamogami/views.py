from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from reservas.models import servicio


class IndexView(ListView):
    model = servicio
    context_object_name = "servicio_list"
    template_name = "kamogami/index.html"


class AboutView(TemplateView):
    template_name = "kamogami/about.html"


class Http404View(TemplateView):
    template_name = "kamogami/404.html"
