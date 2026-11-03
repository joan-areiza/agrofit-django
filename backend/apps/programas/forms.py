from django import forms
from .models import (
    Jornadas,
    Modalidades,
    NivelesFormacionPrograma,
    RequisitosPrograma,
    ProgramasFormacion,
    FichasFormacion,
)


class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornadas
        fields = ["nombre_jornada", "estado_jornada"]


class ModalidadForm(forms.ModelForm):
    class Meta:
        model = Modalidades
        fields = ["nombre_modalidad"]


class NivelFormacionForm(forms.ModelForm):
    class Meta:
        model = NivelesFormacionPrograma
        fields = ["nombre_nivel_formacion_programa"]


class RequisitoProgramaForm(forms.ModelForm):
    class Meta:
        model = RequisitosPrograma
        fields = ["nombre_requisito_programa"]


class ProgramaFormacionForm(forms.ModelForm):
    class Meta:
        model = ProgramasFormacion
        fields = [
            "cod_programa",
            "nombre_programa",
            "id_requisito_programa_fk",
            "duracion_programa",
            "id_centro_formacion_programa_fk",
            "id_nivel_formacion_programa_fk",
            "estado_programa",
        ]


class FichaFormacionForm(forms.ModelForm):
    class Meta:
        model = FichasFormacion
        fields = [
            "numero_ficha",
            "id_programa_ficha_fk",
            "id_jornada_ficha_fk",
            "id_sede_ficha_fk",
            "fecha_inicio_ficha",
            "fecha_fin_ficha",
            "estado_ficha",
            "id_modalidad_ficha_fk",
            "id_instructor_lider_ficha_fk",
        ]
