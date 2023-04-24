import time

import constants
import countdown


def print_account_open_success(user_name: str, user_last_name: str, account_number: int) -> None:
    print(constants.LINE_SEPARATOR)
    print(f" {user_name} {user_last_name}, uspješno ste otvorili račun.")
    print(f" Vaš broj računa je {account_number}")
    print(constants.LINE_SEPARATOR)
    print()


def print_transaction_history(account_number: int, users: dict) -> None:
    print(constants.LINE_SEPARATOR)
    print(f" Povijest transakcija na računu {account_number}")
    print(constants.LINE_SEPARATOR)

    for transaction in users[account_number].get("transaction_history"):
        print(f"{transaction}")
    print()


def print_withdraw_success(withdraw_amount: float, account_number: int) -> None:
    print(constants.LINE_SEPARATOR)
    print(f" Uspješno ste podigli {withdraw_amount} EUR s računa {account_number}!")
    print(constants.LINE_SEPARATOR)
    print()


def print_deposit_success(deposit_amount: float, account_number: int):
    print(constants.LINE_SEPARATOR)
    print(f" Uspješno ste uplatili {deposit_amount} EUR na račun {account_number}!")
    print(constants.LINE_SEPARATOR)
    print()


def print_negative_amount_error() -> None:
    print(constants.LINE_SEPARATOR)
    print(constants.NEGATIVE_AMOUNT_ERROR)
    print(constants.LINE_SEPARATOR)
    print()


def print_invalid_type_error() -> None:
    print(constants.LINE_SEPARATOR)
    print(constants.INVALID_TYPE_ERROR)
    print(constants.LINE_SEPARATOR)
    print()


def print_invalid_oib_error() -> None:
    print(constants.LINE_SEPARATOR)
    print(constants.INVALID_OIB_ERROR)
    print(constants.LINE_SEPARATOR)
    print()


def print_invalid_account_number_error(account_number: int) -> None:
    print(constants.LINE_SEPARATOR)
    print(f" Korisnik s brojem računa {account_number} nije pronađen.")
    print(constants.LINE_SEPARATOR)
    print()


def print_account_balance(account_number: int, users: dict):
    print(constants.LINE_SEPARATOR)
    print(f" Dobar dan {users[account_number].get('user_name')}!\n"
          f" Stanje vašeg računa je {users[account_number].get('account_balance')} EUR")
    print(constants.LINE_SEPARATOR)
    print()


def print_unknown_main_menu_option(user_input: str):
    print()
    print(constants.LINE_SEPARATOR)
    print(f" Unijeli ste '{user_input}' što ne odgovara ni jednoj od ponuđenih opcija.")
    print(constants.LINE_SEPARATOR)
    print()
    print("Povratak na glavni izbornik za: ")
