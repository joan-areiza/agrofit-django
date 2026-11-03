from django.urls import path
from . import views

urlpatterns = [
    path("rutinas/", views.rutinas_list, name="rutinas_list"),
    path("rutinas/<int:rutina_id>/", views.rutina_detail, name="rutina_detail"),
    path("ejercicios/", views.ejercicios_list, name="ejercicios_list"),
    path(
        "ejercicios/<int:ejercicio_id>/",
        views.ejercicio_detail,
        name="ejercicio_detail",
    ),
    path("musculos/", views.musculos_list, name="musculos_list"),
    path("partes-cuerpo/", views.partes_cuerpo_list, name="partes_cuerpo_list"),
    path("objetivos/", views.objetivos_list, name="objetivos_list"),
    path("niveles-rutina/", views.niveles_rutina_list, name="niveles_rutina_list"),
    path("estados-rutina/", views.estados_rutina_list, name="estados_rutina_list"),
    path("complexiones/", views.complexiones_list, name="complexiones_list"),
    path(
        "niveles-actividad/",
        views.niveles_actividad_list,
        name="niveles_actividad_list",
    ),
]
