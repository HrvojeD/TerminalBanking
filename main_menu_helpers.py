from typing import Callable
import constants


def return_to_main_menu_prompt(foo: Callable[[dict], None], users: dict = None):
    user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    while user_input.lower().strip() != "da" and user_input.lower().strip() != "ne":
        print(constants.INVALID_BACK_TO_MAIN_MENU_ANSWER_WARNING)
        user_input = input(constants.BACK_TO_MAIN_MENU_STRING)

    if user_input.lower().strip() == "da":
        return False
    else:
        foo(users)
