import constants
import menu
import open_account
import account_balance
import deposit_funds
import withdraw_funds
import transaction_history
import print_util

users = {}


def run_main_program() -> None:

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
                transaction_history.display_transaction_history(users)
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)

            case "4":
                deposit_funds.deposit_funds(users)
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)

            case "5":
                withdraw_funds.withdraw_funds(users)
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)

            case _:
                print_util.print_unknown_main_menu_option(main_menu_user_choice)
                main_menu_user_choice = menu.display_menu(constants.MAIN_MENU_ITEMS)


run_main_program()
