from django.urls import path
from . import views

urlpatterns = [
    path("usuarios/", views.usuarios_list, name="usuarios_list"),
    path("usuarios/<int:usuario_id>/", views.usuario_detail, name="usuario_detail"),
    path("aprendices/", views.aprendices_list, name="aprendices_list"),
    path(
        "aprendices/<int:aprendiz_id>/", views.aprendiz_detail, name="aprendiz_detail"
    ),
    path("entrenadores/", views.entrenadores_list, name="entrenadores_list"),
    path(
        "entrenadores/<int:entrenador_id>/",
        views.entrenador_detail,
        name="entrenador_detail",
    ),
    path("funcionarios/", views.funcionarios_list, name="funcionarios_list"),
    path("administradores/", views.administradores_list, name="administradores_list"),
    path("fichas-usuarios/", views.fichas_usuarios_list, name="fichas_usuarios_list"),
    path("roles/", views.roles_list, name="roles_list"),
    path("hospitales/", views.hospitales_list, name="hospitales_list"),
    path("eps/", views.eps_list, name="eps_list"),
]
