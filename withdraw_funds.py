import constants


def withdraw_funds(users: dict) -> bool:
    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER))

    if account_number in users.keys():
        user_oib = int(input(constants.ENTER_OIB_PROMPT))

        while len(str(user_oib)) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = int(input(constants.ENTER_OIB_PROMPT))

        if str(user_oib) in str(users[account_number].get("user_oib")):
            try:
                withdraw_amount = float(input(constants.WITHDRAW_FUNDS_PROMPT))

                if withdraw_amount >= 0:
                    users[account_number]["account_balance"] -= withdraw_amount
                    users[account_number]["transaction_history"].append(f" -{withdraw_amount}")
                    print(constants.LINE_SEPARATOR)
                    print(f" Uspješno ste podigli {withdraw_amount} EUR s računa {account_number}!")
                    print(constants.LINE_SEPARATOR)
                    print()
                    withdraw_amount = 0

                else:
                    print(constants.LINE_SEPARATOR)
                    print(constants.INVALID_WITHDRAW_WARNING)
                    print(constants.LINE_SEPARATOR)
                    print()

            except ValueError:
                print(constants.LINE_SEPARATOR)
                print(constants.INVALID_TYPE_ERROR)
                print(constants.LINE_SEPARATOR)
                print()

        else:
            print(constants.LINE_SEPARATOR)
            print(" Unijeli ste netočan OIB.")
            print(constants.LINE_SEPARATOR)
            print()

    else:
        print(constants.LINE_SEPARATOR)
        print(f" Korisnik s brojem računa {account_number} nije pronađen.")
        print(constants.LINE_SEPARATOR)
        print()

    withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while withdraw_funds_user_input.lower().strip() != "da" and withdraw_funds_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if withdraw_funds_user_input.lower().strip() == "da":
        return False
    else:
        withdraw_funds(users)
