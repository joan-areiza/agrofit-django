from .models import Aprendices, Entrenadores, Administradores, Funcionarios, Usuarios


def get_rol(request):
    es_aprendiz = False
    es_entrenador = False
    es_administrador = False
    es_funcionario = False
    rol_nombre = None
    usuario = None

    user = request.user

    if user.is_authenticated:
        if user.is_superuser:
            es_administrador = True
            rol_nombre = "Administrador"
        else:
            usuario = Usuarios.objects.filter(
                correo_usuario__iexact=user.email
            ).first()

            if not usuario:
                usuario = Usuarios.objects.filter(
                    numero_documento_usuario=user.username
                ).first()

            if usuario:
                es_aprendiz = Aprendices.objects.filter(
                    id_usuario_aprendiz_fk=usuario
                ).exists()

                es_entrenador = Entrenadores.objects.filter(
                    id_usuario_entrenador_fk=usuario,
                    estado_entrenador=True,
                ).exists()

                es_administrador = Administradores.objects.filter(
                    id_usuario_administrador_fk=usuario,
                    estado_administrador=True,
                ).exists()

                es_funcionario = Funcionarios.objects.filter(
                    id_usuario_funcionario_fk=usuario
                ).exists()

                if es_administrador:
                    rol_nombre = "Administrador"
                elif es_entrenador:
                    rol_nombre = "Entrenador"
                elif es_funcionario:
                    rol_nombre = "Funcionario"
                elif es_aprendiz:
                    rol_nombre = "Aprendiz"

    return {
        "es_aprendiz": es_aprendiz,
        "es_entrenador": es_entrenador,
        "es_administrador": es_administrador,
        "es_funcionario": es_funcionario,
        "rol_nombre": rol_nombre,
        "usuario": usuario,
    }