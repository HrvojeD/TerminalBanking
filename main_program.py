from constants import MAIN_MENU_ITEMS
from menu import display_menu
from open_account import display_account_opening_options

users = {}


def run_main_program():

    main_menu_user_choice = display_menu(MAIN_MENU_ITEMS)

    while True:
        match main_menu_user_choice.lower().strip():
            case "kraj":
                break
            case "1":
                user_information = display_account_opening_options()
                if user_information:
                    users[user_information.get("account_number")] = user_information
                main_menu_user_choice = display_menu(MAIN_MENU_ITEMS)

            case "2":
                print(2)
            case "3":
                print(3)
            case "4":
                print(4)
            case "5":
                print(5)


run_main_program()
