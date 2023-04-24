import constants
import main_menu_helpers
import print_util
import banking_actions


def withdraw_funds(users: dict) -> None:
    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER).strip())

    if account_number in users.keys():
        user_oib = int(input(constants.ENTER_OIB_PROMPT).strip())

        while len(str(user_oib)) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = int(input(constants.ENTER_OIB_PROMPT))

        if str(user_oib) in str(users[account_number].get("user_oib")):
            banking_actions.withdraw_funds(account_number, users)

        else:
            print_util.print_invalid_oib_error()

    else:
        print_util.print_invalid_account_number_error(account_number)

    main_menu_helpers.return_to_main_menu_prompt(withdraw_funds, users)
