from View_balance import view_balance_screen
from program_rules import *
from database import *

def skrill_dashboard(main_user):
    database = bank_accounts[main_user]

    while True:
        print("SKRILL DASHBOARD")
        print(f"Hello {database['name']}\nWhat would you like to do?\n\n")

        print("[1] View Balance\n[2] Deposit\n[3] Withdraw\n[4] Logout")
        choice = int_rule("ACTION: ")

        if choice is None:
            loading_screen("Invalid input, must be a number.", 1)
            clear_screen()
            continue

        if choice == 1:
            clear_screen()
            from View_balance import view_balance_screen
            return view_balance_screen(main_user)

        elif choice == 2:
            clear_screen()
            from depositmoney import deposit_money
            return deposit_money(main_user)

        elif choice == 3:
            clear_screen()
            from withdrawmoney import withdraw_money
            return withdraw_money(main_user)

        elif choice == 4:
            loading_screen("Logging out...", 1)
            clear_screen()
            from main_menu import menu_screen
            return menu_screen()

        else:
            loading_screen("Invalid input, must be a number or wrong choice.", 1)
            continue









