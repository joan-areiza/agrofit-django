from django.urls import path
from . import views

urlpatterns = [
    path("asignaciones/", views.asignaciones_list, name="asignaciones_list"),
    path(
        "asignaciones/<int:asignacion_id>/",
        views.asignacion_detail,
        name="asignacion_detail",
    ),
    path("asistencias/", views.asistencias_list, name="asistencias_list"),
    path("evaluaciones/", views.evaluaciones_list, name="evaluaciones_list"),
    path(
        "evaluaciones/<int:evaluacion_id>/",
        views.evaluacion_detail,
        name="evaluacion_detail",
    ),
    path("seguimientos/", views.seguimientos_list, name="seguimientos_list"),
    path(
        "seguimientos/<int:seguimiento_id>/",
        views.seguimiento_detail,
        name="seguimiento_detail",
    ),
    path(
        "estados-asignacion/",
        views.estados_asignacion_list,
        name="estados_asignacion_list",
    ),
    path(
        "estados-seguimiento/",
        views.estados_seguimiento_list,
        name="estados_seguimiento_list",
    ),
]
