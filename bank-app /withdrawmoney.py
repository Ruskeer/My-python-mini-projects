from database import *
from program_rules import *
from datetime import datetime

def withdraw_money(current_user):
    database = bank_accounts[current_user]
    transactions = bank_accounts[current_user]["transactions"]
    date = datetime.now().strftime("%Y-%m-%d")


    while True:
        print("WITHDRAWING BOARD")
        print(f"Current Balance: {database['balance']}")

        withdraw = int_rule("Enter the amount you want to withdraw: ")


        if withdraw <= 0 or withdraw > database['balance']:
            print("Invalid amount")
            continue

        purpose = input("Purpose: ").capitalize()

        print("Are you sure you want to proceed? y/n")
        choice = input("ACTION: ").capitalize()
        if choice == "Y":
            database['balance'] -= withdraw

            new_addition = {
                "type": "withdrawal",
                "amount": withdraw,
                "category": purpose,
                "date": date,
            }

            transactions.append(new_addition)
            loading_screen("Successfully withdrawn!", 2)
            clear_screen()

            break

        else:
            break

    from bank_dashboard import skrill_dashboard
    return skrill_dashboard(current_user)



