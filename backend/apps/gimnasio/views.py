from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import TiposMaquina, EstadosMaquina, Maquinas, Horarios


@login_required(login_url="login")
def maquinas_list(request):
    maquinas = Maquinas.objects.select_related(
        "id_estado_maquina_fk", "id_tipo_maquina_fk"
    ).all()
    paginator = Paginator(maquinas, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "gimnasio/maquinas_list.html",
        {
            "title": "Máquinas",
            "maquinas": page_obj,
        },
    )


@login_required(login_url="login")
def maquina_detail(request, maquina_id):
    maquina = get_object_or_404(
        Maquinas.objects.select_related("id_estado_maquina_fk", "id_tipo_maquina_fk"),
        id_maquina_pk=maquina_id,
    )
    return render(
        request,
        "gimnasio/maquina_detail.html",
        {
            "title": maquina.nombre_maquina,
            "maquina": maquina,
        },
    )


@login_required(login_url="login")
def tipos_maquina_list(request):
    tipos = TiposMaquina.objects.all()
    return render(
        request,
        "gimnasio/tipos_maquina_list.html",
        {
            "title": "Tipos de máquina",
            "tipos": tipos,
        },
    )


@login_required(login_url="login")
def estados_maquina_list(request):
    estados = EstadosMaquina.objects.all()
    return render(
        request,
        "gimnasio/estados_maquina_list.html",
        {
            "title": "Estados de máquina",
            "estados": estados,
        },
    )


@login_required(login_url="login")
def horarios_list(request):
    horarios = Horarios.objects.select_related(
        "id_jornada_horario_fk", "id_entrenador_horario_fk"
    ).all()
    paginator = Paginator(horarios, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "gimnasio/horarios_list.html",
        {
            "title": "Horarios",
            "horarios": page_obj,
        },
    )


@login_required(login_url="login")
def horario_detail(request, horario_id):
    horario = get_object_or_404(Horarios, id_horario_pk=horario_id)
    return render(
        request,
        "gimnasio/horario_detail.html",
        {
            "title": f"Horario {horario.id_horario_pk}",
            "horario": horario,
        },
    )
