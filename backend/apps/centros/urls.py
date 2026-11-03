from django.urls import path
from . import views

urlpatterns = [
    path("regiones/", views.regiones_list, name="regiones_list"),
    path("regiones/<int:region_id>/", views.region_detail, name="region_detail"),
    path("departamentos/", views.departamentos_list, name="departamentos_list"),
    path(
        "departamentos/<str:cod_departamento>/",
        views.departamento_detail,
        name="departamento_detail",
    ),
    path("municipios/", views.municipios_list, name="municipios_list"),
    path(
        "municipios/<str:cod_municipio>/",
        views.municipio_detail,
        name="municipio_detail",
    ),
    path("centros/", views.centros_list, name="centros_list"),
    path("centros/<int:centro_id>/", views.centro_detail, name="centro_detail"),
    path("sedes/", views.sedes_list, name="sedes_list"),
    path("sedes/<int:sede_id>/", views.sede_detail, name="sede_detail"),
    path("dependencias/", views.dependencias_list, name="dependencias_list"),
]
