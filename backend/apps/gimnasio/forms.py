from django import forms
from .models import TiposMaquina, EstadosMaquina, Maquinas, Horarios


class TipoMaquinaForm(forms.ModelForm):
    class Meta:
        model = TiposMaquina
        fields = ["nombre_tipo_maquina"]


class EstadoMaquinaForm(forms.ModelForm):
    class Meta:
        model = EstadosMaquina
        fields = ["nombre_estado_maquina"]


class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquinas
        fields = [
            "cod_inventario",
            "nombre_maquina",
            "id_estado_maquina_fk",
            "id_tipo_maquina_fk",
            "descripcion_maquina",
        ]


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = [
            "id_jornada_horario_fk",
            "hora_inicio_horario",
            "hora_fin_horario",
            "cupo_maximo_horario",
            "id_entrenador_horario_fk",
            "estado_horario",
        ]
