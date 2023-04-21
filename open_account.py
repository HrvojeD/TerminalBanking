import random
from constants import *


def display_account_opening_options():

    open_account_user_input = input(BACK_TO_MAIN_MENU_STRING)

    if open_account_user_input.lower().strip() == "da":
        return False

    else:
        print()
        print(LINE_SEPARATOR)

        user_name = input(ENTER_NAME_PROMPT)
        user_last_name = input(ENTER_LAST_NAME)
        user_oib = input(ENTER_OIB_PROMPT)
        if len(user_oib) != 11:
            user_oib = input(ENTER_OIB_PROMPT)

        if (input(IS_DATA_VALID_PROMPT)).lower().strip() == "da":
            account_number = random.randint(9999, 99999)
            print(LINE_SEPARATOR)
            print(f" Vaš broj računa je {account_number}")
            print(LINE_SEPARATOR)

            return {"account_number": account_number,
                    "user_name": user_name,
                    "user_last_name": user_last_name,
                    "user_oib": user_oib}

        else:
            display_account_opening_options()
