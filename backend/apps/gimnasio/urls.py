from django.urls import path
from . import views

urlpatterns = [
    path("maquinas/", views.maquinas_list, name="maquinas_list"),
    path("maquinas/<int:maquina_id>/", views.maquina_detail, name="maquina_detail"),
    path("tipos-maquina/", views.tipos_maquina_list, name="tipos_maquina_list"),
    path("estados-maquina/", views.estados_maquina_list, name="estados_maquina_list"),
    path("horarios/", views.horarios_list, name="horarios_list"),
    path("horarios/<int:horario_id>/", views.horario_detail, name="horario_detail"),
]
