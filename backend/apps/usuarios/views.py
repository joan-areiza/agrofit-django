from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import (
    Usuarios,
    Entrenadores,
    Administradores,
    Funcionarios,
    Aprendices,
    Roles,
    Hospitales,
    Eps,
    FichasUsuarios,
)


@login_required(login_url="login")
def usuarios_list(request):
    usuarios = Usuarios.objects.select_related("id_rol_usuario_fk").all()
    paginator = Paginator(usuarios, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/usuarios_list.html",
        {
            "title": "Usuarios",
            "usuarios": page_obj,
        },
    )


@login_required(login_url="login")
def usuario_detail(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id_usuario_pk=usuario_id)
    return render(
        request,
        "usuarios/usuario_detail.html",
        {
            "title": f"{usuario.nombres_usuario} {usuario.apellidos_usuario}",
            "usuario": usuario,
        },
    )


@login_required(login_url="login")
def aprendices_list(request):
    aprendices = Aprendices.objects.select_related(
        "id_usuario_aprendiz_fk", "id_estado_aprendiz_fk"
    ).all()
    paginator = Paginator(aprendices, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/aprendices_list.html",
        {
            "title": "Aprendices",
            "aprendices": page_obj,
        },
    )


@login_required(login_url="login")
def aprendiz_detail(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendices, id_aprendiz_pk=aprendiz_id)
    return render(
        request,
        "usuarios/aprendiz_detail.html",
        {
            "title": "Detalle aprendiz",
            "aprendiz": aprendiz,
        },
    )


@login_required(login_url="login")
def entrenadores_list(request):
    entrenadores = Entrenadores.objects.select_related(
        "id_usuario_entrenador_fk", "id_especialidad_entrenador_fk"
    ).all()
    paginator = Paginator(entrenadores, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/entrenadores_list.html",
        {
            "title": "Entrenadores",
            "entrenadores": page_obj,
        },
    )


@login_required(login_url="login")
def entrenador_detail(request, entrenador_id):
    entrenador = get_object_or_404(Entrenadores, id_entrenador_pk=entrenador_id)
    return render(
        request,
        "usuarios/entrenador_detail.html",
        {
            "title": "Detalle entrenador",
            "entrenador": entrenador,
        },
    )


@login_required(login_url="login")
def funcionarios_list(request):
    funcionarios = Funcionarios.objects.select_related(
        "id_usuario_funcionario_fk",
        "id_dependencia_funcionario_fk",
        "id_estado_funcionario_fk",
    ).all()
    paginator = Paginator(funcionarios, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/funcionarios_list.html",
        {
            "title": "Funcionarios",
            "funcionarios": page_obj,
        },
    )


@login_required(login_url="login")
def administradores_list(request):
    administradores = Administradores.objects.select_related(
        "id_usuario_administrador_fk", "id_nivel_acceso_administrador_fk"
    ).all()
    paginator = Paginator(administradores, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/administradores_list.html",
        {
            "title": "Administradores",
            "administradores": page_obj,
        },
    )


@login_required(login_url="login")
def fichas_usuarios_list(request):
    fichas = FichasUsuarios.objects.select_related(
        "id_ficha_fk", "id_usuario_ficha_fk"
    ).all()
    paginator = Paginator(fichas, 15)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/fichas_usuarios_list.html",
        {
            "title": "Fichas de usuarios",
            "fichas": page_obj,
        },
    )


@login_required(login_url="login")
def roles_list(request):
    roles = Roles.objects.all()
    return render(
        request,
        "usuarios/roles_list.html",
        {
            "title": "Roles",
            "roles": roles,
        },
    )


@login_required(login_url="login")
def hospitales_list(request):
    hospitales = Hospitales.objects.all()
    paginator = Paginator(hospitales, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/hospitales_list.html",
        {
            "title": "Hospitales",
            "hospitales": page_obj,
        },
    )


@login_required(login_url="login")
def eps_list(request):
    eps = Eps.objects.all()
    paginator = Paginator(eps, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "usuarios/eps_list.html",
        {
            "title": "EPS",
            "eps": page_obj,
        },
    )
