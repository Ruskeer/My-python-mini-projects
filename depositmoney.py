import login_data
from database import *
from program_rules import *
from datetime import datetime

def deposit_money(current_user):
    database = bank_accounts[current_user]
    transactions = bank_accounts[current_user]['transactions']
    date = datetime.now().strftime("%Y-%m-%d")

    while True:
        print("----DEPOSITING BOARD----")
        print(f"Current Balance : {database['balance']}")

        print("Enter the amount you want to deposit")
        deposit = int_rule("AMOUNT: ")

        if deposit < 0:
            loading_screen("Invalid amount, must be greater than 0. Please Try again.",3)
            continue


        purpose = input("Purpose: ").capitalize()

        print(f"Are you sure you want to deposite money with the amount of {deposit}? PRESS ENTER TO CONTINUE / ENTER NO IF YOU CHANGE YOUR MIND. ")
        choice = input("ACTION: ")

        if choice == "":

            database['balance'] += deposit

            new_addition = {
                "type" : "deposit",
                "amount" : deposit,
                "category" : purpose,
                "date" : date,
            }

            transactions.append(new_addition)
            break

        else:
            loading_screen("Going back to dashboard....", 1)
            break


    from bank_dashboard import skrill_dashboard
    return skrill_dashboard(current_user)



