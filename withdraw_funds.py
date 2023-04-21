import constants


def withdraw_funds(users: dict):

    withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while withdraw_funds_user_input.lower().strip() != "da" and withdraw_funds_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        withdraw_funds_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if withdraw_funds_user_input.lower().strip() == "da":
        return False

    else:
        print(constants.LINE_SEPARATOR)
        account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER))

        if account_number in users.keys():

            user_oib = int(input(constants.ENTER_OIB_PROMPT))
            while len(str(user_oib)) != 11:
                print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
                user_oib = int(input(constants.ENTER_OIB_PROMPT))

            if str(user_oib) in str(users[account_number].get("user_oib")):

                withdraw_amount = int(input(constants.WITHDRAW_FUNDS_PROMPT))
                if withdraw_amount >= 0:
                    users[account_number]["account_balance"] -= withdraw_amount
                    print(constants.LINE_SEPARATOR)
                    print(f"Uspješno ste podigli {withdraw_amount} EUR s računa {account_number}!")
                    print(constants.LINE_SEPARATOR)
                    withdraw_amount = 0

                else:
                    print(constants.LINE_SEPARATOR)
                    print(constants.INVALID_DEPOSIT_WARNING)
                    print(constants.LINE_SEPARATOR)
            else:
                print(constants.LINE_SEPARATOR)
                print(" Unijeli ste netočan OIB.")
                print(constants.LINE_SEPARATOR)

        else:
            print(constants.LINE_SEPARATOR)
            print(f" Korisnik s brojem računa {account_number} nije pronađen.")
            print(constants.LINE_SEPARATOR)

        withdraw_funds(users)
