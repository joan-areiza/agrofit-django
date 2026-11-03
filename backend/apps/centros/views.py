from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import (
    Regiones,
    Departamentos,
    Municipios,
    CentrosFormacion,
    Sedes,
    DependenciasFuncionario,
)


@login_required(login_url="login")
def regiones_list(request):
    regiones = Regiones.objects.all()
    paginator = Paginator(regiones, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    return render(
        request,
        "centros/regiones_list.html",
        {
            "title": "Regiones",
            "regiones": page_obj,
        },
    )


@login_required(login_url="login")
def region_detail(request, region_id):
    region = get_object_or_404(Regiones, id_region_pk=region_id)
    return render(
        request,
        "centros/region_detail.html",
        {
            "title": region.nombre_region,
            "region": region,
        },
    )


@login_required(login_url="login")
def departamentos_list(request):
    departamentos = Departamentos.objects.select_related(
        "id_region_departamento_fk"
    ).all()
    paginator = Paginator(departamentos, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "centros/departamentos_list.html",
        {
            "title": "Departamentos",
            "departamentos": page_obj,
        },
    )


@login_required(login_url="login")
def departamento_detail(request, cod_departamento):
    departamento = get_object_or_404(
        Departamentos, cod_departamento_pk=cod_departamento
    )
    municipios = Municipios.objects.filter(cod_departamento_municipio_fk=departamento)
    return render(
        request,
        "centros/departamento_detail.html",
        {
            "title": departamento.nombre_departamento,
            "departamento": departamento,
            "municipios": municipios,
        },
    )


@login_required(login_url="login")
def municipios_list(request):
    municipios = Municipios.objects.select_related(
        "cod_departamento_municipio_fk"
    ).all()
    paginator = Paginator(municipios, 20)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "centros/municipios_list.html",
        {
            "title": "Municipios",
            "municipios": page_obj,
        },
    )


@login_required(login_url="login")
def municipio_detail(request, cod_municipio):
    municipio = get_object_or_404(Municipios, cod_municipio_pk=cod_municipio)
    return render(
        request,
        "centros/municipio_detail.html",
        {
            "title": municipio.nombre_municipio,
            "municipio": municipio,
        },
    )


@login_required(login_url="login")
def centros_list(request):
    centros = CentrosFormacion.objects.select_related("cod_municipio_centro_fk").all()
    paginator = Paginator(centros, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "centros/centros_list.html",
        {
            "title": "Centros de formación",
            "centros": page_obj,
        },
    )


@login_required(login_url="login")
def centro_detail(request, centro_id):
    centro = get_object_or_404(CentrosFormacion, id_centro_pk=centro_id)
    sedes = Sedes.objects.filter(id_centro_sede_fk=centro)
    dependencias = DependenciasFuncionario.objects.filter(
        id_centro_dependencia_fk=centro
    )
    return render(
        request,
        "centros/centro_detail.html",
        {
            "title": centro.nombre_centro,
            "centro": centro,
            "sedes": sedes,
            "dependencias": dependencias,
        },
    )


@login_required(login_url="login")
def sedes_list(request):
    sedes = Sedes.objects.select_related("id_centro_sede_fk").all()
    paginator = Paginator(sedes, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "centros/sedes_list.html",
        {
            "title": "Sedes",
            "sedes": page_obj,
        },
    )


@login_required(login_url="login")
def sede_detail(request, sede_id):
    sede = get_object_or_404(Sedes, id_sede_pk=sede_id)
    return render(
        request,
        "centros/sede_detail.html",
        {
            "title": sede.nombre_sede,
            "sede": sede,
        },
    )


@login_required(login_url="login")
def dependencias_list(request):
    dependencias = DependenciasFuncionario.objects.select_related(
        "id_centro_dependencia_fk"
    ).all()
    paginator = Paginator(dependencias, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "centros/dependencias_list.html",
        {
            "title": "Dependencias",
            "dependencias": page_obj,
        },
    )
