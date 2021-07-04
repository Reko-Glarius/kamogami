from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django import forms
from usuarios.models import User
from usuarios.forms import CreateUserForm, EditUserForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    template_name = "usuarios/registrousuario.html"
    return render(request, template_name, context={})


@login_required
def perfil(request):
    form = EditUserForm(instance=request.user)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            if not form.has_changed():
                messages.error(request, "No realizaste cambios.")
                return redirect("perfil")
            form.save()
            messages.success(request, "Tu datos se actualizaron correctamente.")
        
        else:
            return render(request, "usuarios/modificardatos.html", context={"form": form})

        return redirect("perfil")

    context = {"form": form}
    return render(request, "usuarios/modificardatos.html", context=context)
