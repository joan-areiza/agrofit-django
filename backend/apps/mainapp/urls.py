from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de/", views.about, name="about"),
    path("login/", views.login_view, name="login"),
    path("registro/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/aprendiz/", views.learner_dashboard, name="learner_dashboard"),
    path("dashboard/entrenador/", views.coach_dashboard, name="coach_dashboard"),
    path("dashboard/funcionario/", views.staff_dashboard, name="staff_dashboard"),
    path("dashboard/administrador/", views.admin_dashboard, name="admin_dashboard"),
]