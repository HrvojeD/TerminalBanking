import constants


def deposit_funds(users: dict):

    deposit_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if deposit_funds_user_input.lower().strip() == "da":
        return False

    else:
        print(constants.LINE_SEPARATOR)
        account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER))

        if account_number in users.keys():
            deposit_amount = int(input(constants.DEPOSIT_FUNDS_PROMPT))
            if deposit_amount >= 0:
                users[account_number]["account_balance"] += deposit_amount
                print(constants.LINE_SEPARATOR)
                print(f"Uspješno ste uplatili {deposit_amount} EUR na račun {account_number}!")
                print(constants.LINE_SEPARATOR)
                deposit_amount = 0

            else:
                print(constants.LINE_SEPARATOR)
                print(constants.INVALID_DEPOSIT_WARNING)
                print(constants.LINE_SEPARATOR)

        else:
            print(constants.LINE_SEPARATOR)
            print(f" Korisnik s brojem računa {account_number} nije pronađen.")
            print(constants.LINE_SEPARATOR)

        deposit_funds(users)
