from django import forms
from .models import MensajesContacto, AtencionMensajes


class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model = MensajesContacto
        fields = [
            "nombres_remitente",
            "correo_remitente",
            "titulo_mensaje",
            "contenido_mensaje",
        ]


class AtencionMensajeForm(forms.ModelForm):
    class Meta:
        model = AtencionMensajes
        fields = ["id_mensaje_fk", "id_estado_fk", "observacion"]
