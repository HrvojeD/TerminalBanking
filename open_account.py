import random
import constants


def display_account_opening_options():

    open_account_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while open_account_user_input.lower().strip() != "da" and open_account_user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        open_account_user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if open_account_user_input.lower().strip() == "da":
        return False

    else:
        print(constants.LINE_SEPARATOR)

        user_name = input(constants.ENTER_NAME_PROMPT)
        user_last_name = input(constants.ENTER_LAST_NAME)
        user_oib = input(constants.ENTER_OIB_PROMPT)
        while len(user_oib) != 11:
            print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
            user_oib = input(constants.ENTER_OIB_PROMPT)

        if (input(constants.IS_DATA_VALID_PROMPT)).lower().strip() == "da":
            account_number = random.randint(9999, 99999)
            print(constants.LINE_SEPARATOR)
            print(f" Vaš broj računa je {account_number}")
            print(constants.LINE_SEPARATOR)

            return {"account_number": account_number,
                    "user_name": user_name,
                    "user_last_name": user_last_name,
                    "user_oib": user_oib,
                    "account_balance": 0,
                    "transaction_history": []}

        else:
            display_account_opening_options()
