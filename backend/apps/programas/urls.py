from django.urls import path
from . import views

urlpatterns = [
    path("programas/", views.programas_list, name="programas_list"),
    path("programas/<int:programa_id>/", views.programa_detail, name="programa_detail"),
    path("fichas/", views.fichas_list, name="fichas_list"),
    path("fichas/<int:ficha_id>/", views.ficha_detail, name="ficha_detail"),
    path("jornadas/", views.jornadas_list, name="jornadas_list"),
    path("modalidades/", views.modalidades_list, name="modalidades_list"),
    path("niveles/", views.niveles_list, name="niveles_list"),
    path("requisitos/", views.requisitos_list, name="requisitos_list"),
]
