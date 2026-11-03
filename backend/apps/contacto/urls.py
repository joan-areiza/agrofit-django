from django.urls import path
from . import views

urlpatterns = [
    path("mensajes/", views.mensajes_list, name="mensajes_list"),
    path("mensajes/<int:mensaje_id>/", views.mensaje_detail, name="mensaje_detail"),
    path("estados/", views.estados_contacto_list, name="estados_contacto_list"),
    path("enviar/", views.contacto_enviar, name="contacto_enviar"),
]
