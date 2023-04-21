import constants
import menu
import open_account
import account_balance

users = {}


def run_main_program():

    main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)

    while True:
        match main_menu_user_choice.lower().strip():
            case "kraj":
                break
            case "1":
                user_information = open_account.display_account_opening_options()
                if user_information:
                    users[user_information.get("account_number")] = user_information
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)
            case "2":
                account_balance.display_account_balance(users)
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)
            case "3":
                print(3)
            case "4":
                print(4)
            case "5":
                print(5)


run_main_program()
