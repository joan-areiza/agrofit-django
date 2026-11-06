from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EstadosContacto, MensajesContacto


@login_required(login_url="login")
def mensajes_list(request):
    mensajes = (
        MensajesContacto.objects.select_related("id_estado_contacto_fk")
        .all()
        .order_by("-fecha_envio")
    )
    paginator = Paginator(mensajes, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "contacto/mensajes_list.html",
        {
            "title": "Mensajes de contacto",
            "mensajes": page_obj,
        },
    )


@login_required(login_url="login")
def mensaje_detail(request, mensaje_id):
    mensaje = get_object_or_404(
        MensajesContacto.objects.select_related("id_estado_contacto_fk"),
        id_mensaje_pk=mensaje_id,
    )
    return render(
        request,
        "contacto/mensaje_detail.html",
        {
            "title": mensaje.titulo_mensaje,
            "mensaje": mensaje,
        },
    )


@login_required(login_url="login")
def estados_contacto_list(request):
    estados = EstadosContacto.objects.all()
    return render(
        request,
        "contacto/estados_list.html",
        {
            "title": "Estados de contacto",
            "estados": estados,
        },
    )

def contacto_enviar(request):
    if request.method == "POST":
        nombres = request.POST.get("nombres_remitente", "").strip()
        correo = request.POST.get("correo_remitente", "").strip()
        titulo = request.POST.get("titulo_mensaje", "").strip()
        contenido = request.POST.get("contenido_mensaje", "").strip()

        if nombres and correo and titulo and contenido:
            estado = (
                EstadosContacto.objects.filter(nombre_estado__iexact="Pendiente").first()
            )
            if not estado:
                messages.error(
                    request,
                    "No hay estados de contacto en la base de datos. Crea al menos uno (ej. Pendiente).",
                )
                return redirect("contacto_enviar")

            MensajesContacto.objects.create(
                nombres_remitente=nombres,
                correo_remitente=correo,
                titulo_mensaje=titulo,
                contenido_mensaje=contenido,
                id_estado_contacto_fk=estado,
            )
            messages.success(
                request,
                "Tu mensaje ha sido enviado exitosamente. Pronto nos pondremos en contacto contigo.",
            )
            return redirect("contacto_enviar")

        messages.warning(request, "Por favor diligencia todos los campos del formulario.")

    return render(request, "contacto/contact.html", {"title": "Contacto"})