from django.contrib import admin
from .models import EstadosContacto, MensajesContacto, AtencionMensajes


class EstadosContactoAdmin(admin.ModelAdmin):
    list_display = ("id_estado_contacto_pk", "nombre_estado")
    search_fields = ("nombre_estado",)


class MensajesContactoAdmin(admin.ModelAdmin):
    list_display = (
        "id_mensaje_pk",
        "nombres_remitente",
        "correo_remitente",
        "titulo_mensaje",
        "fecha_envio",
        "id_estado_contacto_fk",
    )
    list_filter = ("id_estado_contacto_fk", "fecha_envio")
    search_fields = (
        "nombres_remitente",
        "correo_remitente",
        "titulo_mensaje",
        "contenido_mensaje",
    )
    date_hierarchy = "fecha_envio"
    readonly_fields = ("fecha_envio",)


class AtencionMensajesAdmin(admin.ModelAdmin):
    list_display = (
        "id_atencion_mensajes_pk",
        "id_mensaje_fk",
        "id_administrador_fk",
        "id_estado_fk",
        "fecha",
    )
    list_filter = ("id_estado_fk", "fecha")
    search_fields = (
        "observacion",
        "id_mensaje_fk__titulo_mensaje",
        "id_mensaje_fk__nombres_remitente",
    )
    date_hierarchy = "fecha"
    readonly_fields = ("fecha", "id_administrador_fk")


admin.site.register(EstadosContacto, EstadosContactoAdmin)
admin.site.register(MensajesContacto, MensajesContactoAdmin)
admin.site.register(AtencionMensajes, AtencionMensajesAdmin)
