import constants
import print_util


def deposit_funds(users: dict) -> bool:

    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER).strip())

    if account_number in users.keys():
        try:
            deposit_amount = float(input(constants.DEPOSIT_FUNDS_PROMPT))

            if deposit_amount >= 0:
                users[account_number]["account_balance"] += deposit_amount
                users[account_number]["transaction_history"].append(f" +{deposit_amount}")
                print_util.print_deposit_success(deposit_amount, account_number)
                deposit_amount = 0

            else:
                print_util.print_negative_amount_error()

        except ValueError:
            print_util.print_invalid_type_error()

    else:
        print_util.print_invalid_account_number_error(account_number)

    deposit_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while deposit_funds_user_input.lower().strip() != "da" and deposit_funds_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        deposit_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if deposit_funds_user_input.lower().strip() == "da":
        return False
    else:
        deposit_funds(users)
