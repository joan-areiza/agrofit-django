from backend.cli.learner_menu import learner_menu
from backend.cli.coach_menu import coach_menu
from backend.cli.staff_menu import staff_menu
from backend.cli.admin_menu import admin_menu


def show_role_menu(role, user):

    menus = {1: learner_menu, 2: coach_menu, 3: staff_menu, 4: admin_menu}

    menu = menus.get(role)

    if menu:
        menu(user)
    else:
        print("\n✕ El usuario no tiene un rol válido.")
