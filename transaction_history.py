import constants


def display_transaction_history(users:dict):

    print(constants.LINE_SEPARATOR)
    account_number: int = int(input(constants.ENTER_ACCOUNT_NUMBER))

    if account_number in users.keys():
        user_oib = int(input(constants.ENTER_OIB_PROMPT))

        while len(str(user_oib)) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = int(input(constants.ENTER_OIB_PROMPT))

        if str(user_oib) in str(users[account_number].get("user_oib")):
            print(constants.LINE_SEPARATOR)
            print(f" Povijest transakcija na računu {account_number}")
            print(constants.LINE_SEPARATOR)

            for transaction in users[account_number].get("transaction_history"):
                print(f"{transaction}")
            print()

    transaction_history_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while transaction_history_user_input.lower().strip() != "da" and transaction_history_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        transaction_history_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if transaction_history_user_input.lower().strip() == "da":
        return False
    else:
        display_transaction_history(users)
