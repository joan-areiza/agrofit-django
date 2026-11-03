from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import (
    EstadosRutina,
    NivelesActividadFisica,
    NivelesRutina,
    ObjetivosRutina,
    PartesCuerpo,
    Musculos,
    Ejercicios,
    Rutinas,
    DetallesRutina,
    ComplexionesFisicas,
)


@login_required(login_url="login")
def rutinas_list(request):
    rutinas = Rutinas.objects.select_related(
        "id_objetivo_rutina_fk", "id_nivel_rutina_fk", "id_estado_rutina_fk"
    ).all()
    paginator = Paginator(rutinas, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "rutinas/rutinas_list.html",
        {
            "title": "Rutinas",
            "rutinas": page_obj,
        },
    )


@login_required(login_url="login")
def rutina_detail(request, rutina_id):
    rutina = get_object_or_404(Rutinas, id_rutina_pk=rutina_id)
    detalles = DetallesRutina.objects.filter(id_rutina_fk=rutina).select_related(
        "id_ejercicio_rutina_fk"
    )
    return render(
        request,
        "rutinas/rutina_detail.html",
        {
            "title": rutina.nombre_rutina,
            "rutina": rutina,
            "detalles": detalles,
        },
    )


@login_required(login_url="login")
def ejercicios_list(request):
    ejercicios = Ejercicios.objects.select_related(
        "id_musculo_ejercicio_fk", "id_maquina_ejercicio_fk"
    ).all()
    paginator = Paginator(ejercicios, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "rutinas/ejercicios_list.html",
        {
            "title": "Ejercicios",
            "ejercicios": page_obj,
        },
    )


@login_required(login_url="login")
def ejercicio_detail(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicios, id_ejercicio_pk=ejercicio_id)
    return render(
        request,
        "rutinas/ejercicio_detail.html",
        {
            "title": ejercicio.nombre_ejercicio,
            "ejercicio": ejercicio,
        },
    )


@login_required(login_url="login")
def musculos_list(request):
    musculos = Musculos.objects.select_related("id_parte_cuerpo_musculo_fk").all()
    paginator = Paginator(musculos, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "rutinas/musculos_list.html",
        {
            "title": "Músculos",
            "musculos": page_obj,
        },
    )


@login_required(login_url="login")
def partes_cuerpo_list(request):
    partes = PartesCuerpo.objects.all()
    return render(
        request,
        "rutinas/partes_cuerpo_list.html",
        {
            "title": "Partes del cuerpo",
            "partes": partes,
        },
    )


@login_required(login_url="login")
def objetivos_list(request):
    objetivos = ObjetivosRutina.objects.all()
    return render(
        request,
        "rutinas/objetivos_list.html",
        {
            "title": "Objetivos de rutina",
            "objetivos": objetivos,
        },
    )


@login_required(login_url="login")
def niveles_rutina_list(request):
    niveles = NivelesRutina.objects.all()
    return render(
        request,
        "rutinas/niveles_rutina_list.html",
        {
            "title": "Niveles de rutina",
            "niveles": niveles,
        },
    )


@login_required(login_url="login")
def estados_rutina_list(request):
    estados = EstadosRutina.objects.all()
    return render(
        request,
        "rutinas/estados_rutina_list.html",
        {
            "title": "Estados de rutina",
            "estados": estados,
        },
    )


@login_required(login_url="login")
def complexiones_list(request):
    complexiones = ComplexionesFisicas.objects.all()
    return render(
        request,
        "rutinas/complexiones_list.html",
        {
            "title": "Complexiones físicas",
            "complexiones": complexiones,
        },
    )


@login_required(login_url="login")
def niveles_actividad_list(request):
    niveles = NivelesActividadFisica.objects.all()
    return render(
        request,
        "rutinas/niveles_actividad_list.html",
        {
            "title": "Niveles de actividad física",
            "niveles": niveles,
        },
    )
