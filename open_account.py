import random
from typing import Union
import constants
import main_menu_helpers
import print_util


def display_account_opening_options() -> Union[dict, None]:

    print(constants.LINE_SEPARATOR)
    user_name = input(constants.ENTER_NAME_PROMPT)
    user_last_name = input(constants.ENTER_LAST_NAME)
    user_oib = input(constants.ENTER_OIB_PROMPT)

    while len(user_oib) != 11:
        print(constants.NOT_ENOUGH_DIGITS_OIB_WARNING)
        user_oib = input(constants.ENTER_OIB_PROMPT)

    if (input(constants.IS_DATA_VALID_PROMPT)).lower().strip() == "da":
        account_number = random.randint(9999, 99999)
        print_util.print_account_open_success(user_name, user_last_name, account_number)
        return {"account_number": account_number,
                "user_name": user_name,
                "user_last_name": user_last_name,
                "user_oib": user_oib,
                "account_balance": 0,
                "transaction_history": []}

    main_menu_helpers.return_to_main_menu_prompt(display_account_opening_options)
