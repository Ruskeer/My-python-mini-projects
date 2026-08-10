from database import *
from program_rules import *

def view_balance_screen(current_user):

    database_history = bank_accounts[current_user]['transactions']



    while True:
        #------if the transaction history is empty--
        if not database_history:
            loading_screen("There is nothing to see here.", 2)
            clear_screen()
            from bank_dashboard import skrill_dashboard
            return skrill_dashboard(current_user)

        else:

            print("-------BANK HISTORY--------")
            print("[1] Deposit History\n[2] Withdrawal History\n[3] Return to Dashboard")
            choice = int_rule("ACTION: ")

            ##---Deposit history logic---
            if choice == 1:

                print("DEPOSIT HISTORY/TRANSACTION")
                transactionID = 10000
                for each in database_history:
                    if each['type'] == 'deposit':
                        print(f"{transactionID} ---- DEPOSITED : {each['amount']}        CATEGORY: {each['category']}          DATE: {each['date']} ")
                        transactionID += 20


            ##---Withdraw history logic---
            elif choice == 2:

                print("WITHDRAWAL HISTORY/TRANSACTION")
                transactionID = 10000
                for each in database_history:
                    if each['type'] == 'withdrawal':
                        print(f"{transactionID} ---- WITHDRAWED : {each['amount']}        CATEGORY: {each['category']}          DATE: {each['date']} ")
                        transactionID += 20


            ##-- Going back to dashboard
            elif choice == 3:

                clear_screen()
                from bank_dashboard import skrill_dashboard
                return skrill_dashboard(current_user)



            if choice is None:
                print("Invalid input, must be a number.")


        continue




