from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required
from datetime import datetime

from apps.usuarios.models import (
    Usuarios,
    TiposDocumento,
    Sexos,
    TiposSangre,
    EstadosCivil,
    Eps,
    Hospitales,
    Roles,
    Aprendices,
    Entrenadores,
    Funcionarios,
    Administradores,
    EstadosAprendiz,
    EspecialidadesEntrenador,
    
    EstadosFuncionario,
)
from apps.centros.models import(
    Departamentos,
    Municipios,
    DependenciasFuncionario,
)
def index(request):
    """Página de inicio (landing page)."""
    return render(request, "mainapp/index.html")


def login_view(request):
    if request.method == "POST":
        num_doc = request.POST.get("login-num-document")
        password = request.POST.get("login-password")

        # 1. Autenticación estándar en Django Auth (username = numero_documento)
        user = authenticate(request, username=num_doc, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            # 2. Consultar perfil en la tabla 'usuarios' de la BD
            usuario = Usuarios.objects.filter(numero_documento_usuario=user.username).first()

            if usuario:
                # Redirección dinámica basada en la subtabla asociada
                if Administradores.objects.filter(id_usuario_administrador_fk=usuario, estado_administrador=True).exists():
                    return redirect("admin_dashboard")
                if Entrenadores.objects.filter(id_usuario_entrenador_fk=usuario, estado_entrenador=True).exists():
                    return redirect("coach_dashboard")
                if Funcionarios.objects.filter(id_usuario_funcionario_fk=usuario).exists():
                    return redirect("staff_dashboard")
                if Aprendices.objects.filter(id_usuario_aprendiz_fk=usuario).exists():
                    return redirect("learner_dashboard")

            return redirect("index")
        else:
            messages.error(request, "Número de documento o contraseña incorrectos.")

    return redirect("index")

def register_view(request):
    if request.method == "POST":
        # Formulario modal
        rol_codigo = request.POST.get("register-rol")  # 'APR', 'ENT', 'FUN'
        tipo_doc_cod = request.POST.get("register-document-type")  # Ej: 'CC', 'TI'
        num_doc = request.POST.get("register-num-document")
        birthday = request.POST.get("birthday")
        nombres = request.POST.get("name")
        apellidos = request.POST.get("last-name", "")
        genero_cod = request.POST.get("genre")  # Ej: 'M', 'F'
        estado_civil_id = request.POST.get("marital-status")  # ID de estado_civil
        tipo_sangre_cod = request.POST.get("register-blood-type")  # Ej: 'A+'
        discapacidad = request.POST.get("health")
        correo = request.POST.get("email-register")
        password = request.POST.get("password-register")
        confirm_password = request.POST.get("confirm-password-register")
        telefono = request.POST.get("phone")
        municipio_cod = request.POST.get("mun")  # Código de municipio ej: '019001'
        direccion = request.POST.get("dir")
        eps_cod = request.POST.get("eps")  # Código de EPS ej: 'EPS001'

        if password and confirm_password and password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("index")

        if User.objects.filter(username=num_doc).exists():
            messages.error(request, "El número de documento ya se encuentra registrado.")
            return redirect("index")

        try:
            with transaction.atomic():
                # A. Crear usuario base de Django Auth
                user = User.objects.create_user(
                    username=num_doc,
                    email=correo,
                    password=password,
                    first_name=nombres,
                    last_name=apellidos
                )

                # B. Obtener las instancias FK de la BD real
                tipo_doc_obj = TiposDocumento.objects.filter(cod_tipo_documento_pk=tipo_doc_cod).first() or TiposDocumento.objects.first()
                sexo_obj = Sexos.objects.filter(cod_sexo_pk=genero_cod).first() or Sexos.objects.first()
                tipo_sangre_obj = TiposSangre.objects.filter(cod_tipo_sangre_pk=tipo_sangre_cod).first() or TiposSangre.objects.first()
                
                estado_civil_obj = None
                if estado_civil_id and str(estado_civil_id).isdigit():
                    estado_civil_obj = EstadosCivil.objects.filter(id_estado_civil_pk=int(estado_civil_id)).first()
                if not estado_civil_obj:
                    estado_civil_obj = EstadosCivil.objects.first()

                # Departamento y Municipio predeterminados (ej: Cauca / Popayán si no especifica)
                municipio_obj = Municipios.objects.filter(cod_municipio_pk=municipio_cod).first() or Municipios.objects.filter(cod_municipio_pk="019001").first()
                departamento_obj = municipio_obj.cod_departamento_municipio_fk if municipio_obj else Departamentos.objects.first()

                eps_obj = Eps.objects.filter(cod_eps_pk=eps_cod).first() or Eps.objects.first()
                hospital_obj = Hospitales.objects.first()  # Asigna el hospital predeterminado

                # Mapeo del Rol
                rol_map = {'APR': 'APRENDIZ', 'ENT': 'ENTRENADOR', 'FUN': 'FUNCIONARIO'}
                nombre_rol_busqueda = rol_map.get(rol_codigo, 'APRENDIZ')
                rol_obj = Roles.objects.filter(nombre_rol__iexact=nombre_rol_busqueda).first() or Roles.objects.first()

                # C. Guardar registro en la tabla 'usuarios'
                usuario = Usuarios.objects.create(
                    numero_documento_usuario=num_doc,
                    cod_tipo_documento_usuario_fk=tipo_doc_obj,
                    correo_usuario=correo,
                    telefono_usuario=telefono,
                    clave_usuario=user.password,  # Hash generado por Django
                    nombres_usuario=nombres,
                    apellidos_usuario=apellidos,
                    cod_sexo_usuario_fk=sexo_obj,
                    cod_tipo_sangre_usuario_fk=tipo_sangre_obj,
                    fecha_nacimiento_usuario=birthday if birthday else "2000-01-01",
                    id_estado_civil_usuario_fk=estado_civil_obj,
                    cod_departamento_usuario_fk=departamento_obj,
                    cod_municipio_usuario_fk=municipio_obj,
                    direccion_usuario=direccion if direccion else "Popayán",
                    fecha_registro_usuario=datetime.now(),
                    estado_usuario=1,
                    id_rol_usuario_fk=rol_obj,
                    cod_hospital_usuario_fk=hospital_obj,
                    cod_eps_usuario_fk=eps_obj
                )

                # D. Vincular a la subtabla según el Rol seleccionado
                if rol_codigo == "APR":
                    estado_apr = EstadosAprendiz.objects.first()
                    Aprendices.objects.create(
                        id_usuario_aprendiz_fk=usuario,
                        id_estado_aprendiz_fk=estado_apr
                    )
                elif rol_codigo == "ENT":
                    esp_ent = EspecialidadesEntrenador.objects.first()
                    Entrenadores.objects.create(
                        id_usuario_entrenador_fk=usuario,
                        id_especialidad_entrenador_fk=esp_ent,
                        estado_entrenador=1
                    )
                elif rol_codigo == "FUN":
                    dep_fun = DependenciasFuncionario.objects.first()
                    est_fun = EstadosFuncionario.objects.first()
                    Funcionarios.objects.create(
                        id_usuario_funcionario_fk=usuario,
                        id_dependencia_funcionario_fk=dep_fun,
                        id_estado_funcionario_fk=est_fun
                    )

                login(request, user)
                messages.success(request, "Registro completado exitosamente.")

                if rol_codigo == "APR":
                    return redirect("learner_dashboard")
                elif rol_codigo == "ENT":
                    return redirect("coach_dashboard")
                elif rol_codigo == "FUN":
                    return redirect("staff_dashboard")

        except Exception as e:
            messages.error(request, f"Ocurrió un error al procesar el registro: {str(e)}")

    return redirect("index")

def logout_view(request):
    logout(request)
    return redirect("index")

def about(request):
    """Renderiza la página de Acerca De."""
    return render(request, "mainapp/about.html")

@login_required(login_url="index")
def learner_dashboard(request):
    usuario = Usuarios.objects.filter(
        numero_documento_usuario=request.user.username
    ).first() or Usuarios.objects.filter(
        correo_usuario__iexact=request.user.email
    ).first()

    es_aprendiz = usuario and Aprendices.objects.filter(
        id_usuario_aprendiz_fk=usuario
    ).exists()

    if not (es_aprendiz or request.user.is_superuser):
        return redirect("index")

    return render(request, "mainapp/dashboards/learner-dashboard.html")

@login_required(login_url="index")
def coach_dashboard(request):
    usuario = Usuarios.objects.filter(
        numero_documento_usuario=request.user.username
    ).first() or Usuarios.objects.filter(
        correo_usuario__iexact=request.user.email
    ).first()

    es_entrenador = usuario and Entrenadores.objects.filter(
        id_usuario_entrenador_fk=usuario, estado_entrenador=True
    ).exists()

    if not (es_entrenador or request.user.is_superuser):
        return redirect("index")

    return render(request, "mainapp/dashboards/coach-dashboard.html")

@login_required(login_url="index")
def staff_dashboard(request):
    usuario = Usuarios.objects.filter(
        numero_documento_usuario=request.user.username
    ).first() or Usuarios.objects.filter(
        correo_usuario__iexact=request.user.email
    ).first()

    es_funcionario = usuario and Funcionarios.objects.filter(
        id_usuario_funcionario_fk=usuario
    ).exists()

    if not (es_funcionario or request.user.is_superuser):
        return redirect("index")

    return render(request, "mainapp/dashboards/staff-dashboard.html")

@login_required(login_url="index")
def admin_dashboard(request):
    usuario = Usuarios.objects.filter(
        numero_documento_usuario=request.user.username
    ).first() or Usuarios.objects.filter(
        correo_usuario__iexact=request.user.email
    ).first()

    es_admin = usuario and Administradores.objects.filter(
        id_usuario_administrador_fk=usuario, estado_administrador=True
    ).exists()

    if not (es_admin or request.user.is_superuser):
        return redirect("index")

    return render(request, "mainapp/dashboards/admin-dashboard.html")