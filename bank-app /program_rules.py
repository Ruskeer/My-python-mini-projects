import time

def int_rule(text):
    user_data = input(text)
    if user_data.isdigit():
        return int(user_data)

    return None

def loading_screen(text, duration):

    print(text)
    time.sleep(duration)

def clear_screen():
    print("\n" * 20)
    time.sleep(1)
