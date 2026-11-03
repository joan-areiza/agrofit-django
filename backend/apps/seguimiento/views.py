from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import (
    EstadosAsignacion,
    AsignacionesRutinaUsuario,
    Asistencias,
    EvaluacionesFisicas,
    EstadosSeguimiento,
    SeguimientosProgresoUsuario,
)


@login_required(login_url="login")
def asignaciones_list(request):
    asignaciones = (
        AsignacionesRutinaUsuario.objects.select_related(
            "id_rutina_fk",
            "id_usuario_fk",
            "id_estado_asignacion_rutina_fk",
            "id_entrenador_asigna_rutina_fk",
        )
        .all()
        .order_by("-fecha_hora_inicio_asignacion_rutina")
    )
    paginator = Paginator(asignaciones, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "seguimiento/asignaciones_list.html",
        {
            "title": "Asignaciones de rutina",
            "asignaciones": page_obj,
        },
    )


@login_required(login_url="login")
def asignacion_detail(request, asignacion_id):
    asignacion = get_object_or_404(
        AsignacionesRutinaUsuario, id_asignacion_rutina_usuario_pk=asignacion_id
    )
    return render(
        request,
        "seguimiento/asignacion_detail.html",
        {
            "title": f"Asignación {asignacion.id_asignacion_rutina_usuario_pk}",
            "asignacion": asignacion,
        },
    )


@login_required(login_url="login")
def asistencias_list(request):
    asistencias = (
        Asistencias.objects.select_related(
            "id_aprendiz_asistencia_fk",
            "id_entrenador_asistencia_fk",
            "id_rutina_asistencia_fk",
        )
        .all()
        .order_by("-fecha_asistencia")
    )
    paginator = Paginator(asistencias, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "seguimiento/asistencias_list.html",
        {
            "title": "Asistencias",
            "asistencias": page_obj,
        },
    )


@login_required(login_url="login")
def evaluaciones_list(request):
    evaluaciones = (
        EvaluacionesFisicas.objects.select_related(
            "id_usuario_evaluacion_fk",
            "id_entrenador_encargado_evaluacion_fk",
        )
        .all()
        .order_by("-fecha_evaluacion")
    )
    paginator = Paginator(evaluaciones, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "seguimiento/evaluaciones_list.html",
        {
            "title": "Evaluaciones físicas",
            "evaluaciones": page_obj,
        },
    )


@login_required(login_url="login")
def evaluacion_detail(request, evaluacion_id):
    evaluacion = get_object_or_404(
        EvaluacionesFisicas, id_evaluacion_fisica_pk=evaluacion_id
    )
    return render(
        request,
        "seguimiento/evaluacion_detail.html",
        {
            "title": f"Evaluación {evaluacion.id_evaluacion_fisica_pk}",
            "evaluacion": evaluacion,
        },
    )


@login_required(login_url="login")
def seguimientos_list(request):
    seguimientos = (
        SeguimientosProgresoUsuario.objects.select_related(
            "id_estado_seguimiento_fk",
            "id_evaluacion_fisica_fk",
            "id_objetivo_actual_fk",
        )
        .all()
        .order_by("-fecha_registro_progreso")
    )
    paginator = Paginator(seguimientos, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "seguimiento/seguimientos_list.html",
        {
            "title": "Seguimientos de progreso",
            "seguimientos": page_obj,
        },
    )


@login_required(login_url="login")
def seguimiento_detail(request, seguimiento_id):
    seguimiento = get_object_or_404(
        SeguimientosProgresoUsuario, id_seguimiento_progreso_usuario_pk=seguimiento_id
    )
    return render(
        request,
        "seguimiento/seguimiento_detail.html",
        {
            "title": f"Seguimiento {seguimiento.id_seguimiento_progreso_usuario_pk}",
            "seguimiento": seguimiento,
        },
    )


@login_required(login_url="login")
def estados_asignacion_list(request):
    estados = EstadosAsignacion.objects.all()
    return render(
        request,
        "seguimiento/estados_asignacion_list.html",
        {
            "title": "Estados de asignación",
            "estados": estados,
        },
    )


@login_required(login_url="login")
def estados_seguimiento_list(request):
    estados = EstadosSeguimiento.objects.all()
    return render(
        request,
        "seguimiento/estados_seguimiento_list.html",
        {
            "title": "Estados de seguimiento",
            "estados": estados,
        },
    )
