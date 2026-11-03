from django import forms
from .models import (
    AsignacionesRutinaUsuario,
    Asistencias,
    EvaluacionesFisicas,
    SeguimientosProgresoUsuario,
)


class AsignacionRutinaForm(forms.ModelForm):
    class Meta:
        model = AsignacionesRutinaUsuario
        fields = [
            "id_rutina_fk",
            "id_usuario_fk",
            "fecha_hora_fin_asignacion_rutina",
            "id_estado_asignacion_rutina_fk",
            "id_entrenador_asigna_rutina_fk",
        ]

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencias
        fields = [
            "id_aprendiz_asistencia_fk",
            "id_entrenador_asistencia_fk",
            "id_rutina_asistencia_fk",
            "estado_asistencia",
        ]


class EvaluacionFisicaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionesFisicas
        fields = [
            "id_usuario_evaluacion_fk",
            "id_entrenador_encargado_evaluacion_fk",
            "peso_evaluacion",
            "altura_evaluacion",
            "grasa_corporal_evaluacion",
            "grasa_muscular_evaluacion",
            "presion_sistolica",
            "presion_diastolica",
            "imc_evaluacion",
            "medida_cintura",
            "medida_cadera",
            "id_nivel_actividad_fisica_evaluacion_fk",
            "id_antecedente_medico_evaluacion_fk",
            "id_complexion_fisica_evaluacion_fk",
            "observacion_evaluacion",
        ]


class SeguimientoProgresoForm(forms.ModelForm):
    class Meta:
        model = SeguimientosProgresoUsuario
        fields = [
            "id_evaluacion_fisica_fk",
            "horas_ludicas",
            "rutinas_completadas",
            "id_estado_seguimiento_fk",
            "id_objetivo_actual_fk",
            "observacion_progreso_usuario",
            "logros_avances",
            "aspectos_a_mejorar",
        ]
