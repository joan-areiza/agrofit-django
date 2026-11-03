from django import forms
from .models import (
    Usuarios,
    Aprendices,
    Entrenadores,
    Funcionarios,
    Administradores,
    FichasUsuarios,
)


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            "numero_documento_usuario",
            "cod_tipo_documento_usuario_fk",
            "correo_usuario",
            "telefono_usuario",
            "telefono_emergencia_usuario",
            "clave_usuario",
            "nombres_usuario",
            "apellidos_usuario",
            "cod_sexo_usuario_fk",
            "cod_tipo_sangre_usuario_fk",
            "fecha_nacimiento_usuario",
            "id_estado_civil_usuario_fk",
            "cod_departamento_usuario_fk",
            "cod_municipio_usuario_fk",
            "direccion_usuario",
            "foto_usuario",
            "estado_usuario",
            "id_rol_usuario_fk",
            "cod_hospital_usuario_fk",
            "cod_eps_usuario_fk",
        ]


class PerfilUsuarioForm(forms.ModelForm):
    """Edición limitada del perfil (sin rol ni estado)."""

    class Meta:
        model = Usuarios
        fields = [
            "telefono_usuario",
            "telefono_emergencia_usuario",
            "direccion_usuario",
            "foto_usuario",
            "cod_municipio_usuario_fk",
            "cod_departamento_usuario_fk",
        ]


class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendices
        fields = ["id_usuario_aprendiz_fk", "id_estado_aprendiz_fk"]


class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenadores
        fields = [
            "id_usuario_entrenador_fk",
            "id_especialidad_entrenador_fk",
            "estado_entrenador",
        ]


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = [
            "id_usuario_funcionario_fk",
            "id_dependencia_funcionario_fk",
            "id_estado_funcionario_fk",
        ]


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administradores
        fields = [
            "id_usuario_administrador_fk",
            "id_nivel_acceso_administrador_fk",
            "estado_administrador",
        ]


class FichaUsuarioForm(forms.ModelForm):
    class Meta:
        model = FichasUsuarios
        fields = ["id_ficha_fk", "id_usuario_ficha_fk", "fecha_inscripcion"]
