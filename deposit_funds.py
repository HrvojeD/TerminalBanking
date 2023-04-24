import banking_actions
import constants
import main_menu_helpers
import print_util


def deposit_funds(users: dict):

    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER).strip())

    if account_number in users.keys():
        banking_actions.deposit_funds(account_number, users)

    else:
        print_util.print_invalid_account_number_error(account_number)

    main_menu_helpers.return_to_main_menu_prompt(deposit_funds, users)
