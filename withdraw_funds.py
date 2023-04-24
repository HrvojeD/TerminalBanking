import constants
import print_util


def withdraw_funds(users: dict) -> bool:
    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER).strip())

    if account_number in users.keys():
        user_oib = int(input(constants.ENTER_OIB_PROMPT).strip())

        while len(str(user_oib)) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = int(input(constants.ENTER_OIB_PROMPT))

        if str(user_oib) in str(users[account_number].get("user_oib")):
            try:
                withdraw_amount = float(input(constants.WITHDRAW_FUNDS_PROMPT))

                if withdraw_amount >= 0:
                    users[account_number]["account_balance"] -= withdraw_amount
                    users[account_number]["transaction_history"].append(f" -{withdraw_amount}")
                    print_util.print_withdraw_success(withdraw_amount, account_number)
                    withdraw_amount = 0

                else:
                    print_util.print_negative_amount_error()

            except ValueError:
                print_util.print_invalid_type_error()

        else:
            print_util.print_invalid_oib_error()

    else:
        print_util.print_invalid_account_number_error(account_number)

    withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while withdraw_funds_user_input.lower().strip() != "da" and withdraw_funds_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if withdraw_funds_user_input.lower().strip() == "da":
        return False
    else:
        withdraw_funds(users)
