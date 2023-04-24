import constants


def display_account_balance(users: dict) -> bool:

    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER).strip())

    if account_number in users.keys():
        user_oib = int(input(constants.ENTER_OIB_PROMPT))

        while len(str(user_oib)) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = int(input(constants.ENTER_OIB_PROMPT))

        if str(user_oib) in str(users[account_number].get("user_oib")):
            print(constants.LINE_SEPARATOR)
            print(f" Dobar dan {users[account_number].get('user_name')}!\n"
                  f" Stanje vašeg računa je {users[account_number].get('account_balance')} EUR")
            print(constants.LINE_SEPARATOR)
            print()

        else:
            print(constants.LINE_SEPARATOR)
            print(" Unijeli ste netočan OIB.")
            print(constants.LINE_SEPARATOR)
            print()

    else:
        print(constants.LINE_SEPARATOR)
        print(f" Korisnik s brojem računa {account_number} nije pronađen")
        print(constants.LINE_SEPARATOR)
        print()

    account_balance_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while account_balance_user_input.lower().strip() != "da" and account_balance_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        account_balance_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if account_balance_user_input.lower().strip() == "da":
        return False
    else:
        display_account_balance(users)
