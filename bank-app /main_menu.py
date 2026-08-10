from program_rules import *

def menu_screen():
    while True:
        print("BANKO DE SKRILL\n")
        print("[1] CREATE BANK ACCOUNT\n[2]PROCEED TO BANK ACCOUNT")
        action = int_rule("ACTION: ")


        if action == 1:

            clear_screen()
            from create_bank import create_account_screen
            return create_account_screen()

        elif action == 2:

            clear_screen()
            from login_data import login_screen
            return login_screen()

        else:

            print("Invalid choice.")
            clear_screen()
            continue


while True:
    menu_screen()



