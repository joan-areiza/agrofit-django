from django import forms
from .models import Rutinas, DetallesRutina, Ejercicios


class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutinas
        fields = [
            "nombre_rutina",
            "id_objetivo_rutina_fk",
            "id_nivel_rutina_fk",
            "id_estado_rutina_fk",
        ]


class DetalleRutinaForm(forms.ModelForm):
    class Meta:
        model = DetallesRutina
        fields = [
            "id_rutina_fk",
            "id_ejercicio_rutina_fk",
            "series_rutina",
            "repeticiones_rutina",
            "carga_rutina",
            "descanso_segundos",
        ]


class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicios
        fields = [
            "nombre_ejercicio",
            "descripcion_ejercicio",
            "url_video_demo_ejercicio",
            "id_maquina_ejercicio_fk",
            "id_musculo_ejercicio_fk",
        ]
