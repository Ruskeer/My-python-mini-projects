from program_rules import *
from database import *
from encrypting import *


def login_screen():
    max_attempt = 3



    print("-" * 7 + "BANK CENTRAL" + "-" * 7)

    while True:

        #----LOGIN LINE with 3 attempts
        for attempt in range(1, max_attempt + 1):
            found_id = False
            id_num = int_rule("ID Number: ")

            ##------looking for existing ID-----
            for correct_id in bank_accounts:
                if correct_id == id_num:
                    found_id = correct_id
                    break

            ##----if ID num is correct, proceed to pincode...
            if found_id:
                pin_num = str(input("Enter the 4 digit pincode: "))
                crypted_pin = encrypting_nu(pin_num, master_key, 'encrypt')

                ###---checking if pincode is correct
                if bank_accounts[found_id]['pin'] == crypted_pin:

                    loading_screen("\nAccessing the data....", 1)
                    from bank_dashboard import skrill_dashboard
                    return skrill_dashboard(found_id)
                ###------
                else:
                    print(f"\nIncorrect pincode. Please try again. Attempts left #{attempt}\n")

            ##-----
            else:
                choice = input("ID code doesn't exist. Would you like to try again? YES/EXIT: ").upper()
                if choice == "YES":
                    break

                else:
                    from main_menu import menu_screen
                    return menu_screen()



