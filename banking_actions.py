import constants
import print_util


def withdraw_funds(account_number: int, users: dict) -> None:
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


def deposit_money(account_number: int, users: dict) -> None:
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
