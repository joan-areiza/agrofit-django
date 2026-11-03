from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import (
    Jornadas,
    Modalidades,
    NivelesFormacionPrograma,
    RequisitosPrograma,
    ProgramasFormacion,
    FichasFormacion,
)


@login_required(login_url="login")
def programas_list(request):
    programas = ProgramasFormacion.objects.select_related(
        "id_requisito_programa_fk",
        "id_centro_formacion_programa_fk",
        "id_nivel_formacion_programa_fk",
    ).all()
    paginator = Paginator(programas, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "programas/programas_list.html",
        {
            "title": "Programas de formación",
            "programas": page_obj,
        },
    )


@login_required(login_url="login")
def programa_detail(request, programa_id):
    programa = get_object_or_404(ProgramasFormacion, id_programa_pk=programa_id)
    fichas = FichasFormacion.objects.filter(id_programa_ficha_fk=programa)
    return render(
        request,
        "programas/programa_detail.html",
        {
            "title": programa.nombre_programa,
            "programa": programa,
            "fichas": fichas,
        },
    )


@login_required(login_url="login")
def fichas_list(request):
    fichas = FichasFormacion.objects.select_related(
        "id_programa_ficha_fk",
        "id_jornada_ficha_fk",
        "id_sede_ficha_fk",
        "id_modalidad_ficha_fk",
    ).all()
    paginator = Paginator(fichas, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "programas/fichas_list.html",
        {
            "title": "Fichas de formación",
            "fichas": page_obj,
        },
    )


@login_required(login_url="login")
def ficha_detail(request, ficha_id):
    ficha = get_object_or_404(FichasFormacion, id_ficha_formacion_pk=ficha_id)
    return render(
        request,
        "programas/ficha_detail.html",
        {
            "title": f"Ficha {ficha.numero_ficha}",
            "ficha": ficha,
        },
    )


@login_required(login_url="login")
def jornadas_list(request):
    jornadas = Jornadas.objects.all()
    return render(
        request,
        "programas/jornadas_list.html",
        {
            "title": "Jornadas",
            "jornadas": jornadas,
        },
    )


@login_required(login_url="login")
def modalidades_list(request):
    modalidades = Modalidades.objects.all()
    return render(
        request,
        "programas/modalidades_list.html",
        {
            "title": "Modalidades",
            "modalidades": modalidades,
        },
    )


@login_required(login_url="login")
def niveles_list(request):
    niveles = NivelesFormacionPrograma.objects.all()
    return render(
        request,
        "programas/niveles_list.html",
        {
            "title": "Niveles de formación",
            "niveles": niveles,
        },
    )


@login_required(login_url="login")
def requisitos_list(request):
    requisitos = RequisitosPrograma.objects.all()
    return render(
        request,
        "programas/requisitos_list.html",
        {
            "title": "Requisitos",
            "requisitos": requisitos,
        },
    )
