import time


def display_countdown(seconds: int):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(0.8)
