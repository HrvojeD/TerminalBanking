from constants import MAIN_MENU_ITEMS
from menu import display_menu


def run_main_program():
    while True:
        user_choice = display_menu(MAIN_MENU_ITEMS)

        if user_choice == "kraj":
            break


run_main_program()
