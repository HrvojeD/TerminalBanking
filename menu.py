from constants import MAIN_MENU_USER_PROMPT
from constants import LINE_SEPARATOR


def display_menu(menu_type: dict) -> str:

    print()
    print(f"{menu_type.get('0'):^32}")
    print(LINE_SEPARATOR)
    for key, value in menu_type.items():
        if key == "0":
            continue
        print(f"| {key}{'.':<3} {value:<25} |")
    print(LINE_SEPARATOR)
    print()
    return input(MAIN_MENU_USER_PROMPT)
