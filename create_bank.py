from database import *
from program_rules import *
from encrypting import *

def create_account_screen():

    #-----------------------------------------------------------------
    #this condition exist for the purpose whether the user want to change the username
    while True:
        print("-----SIGN UP-----")
        # Input full name
        full_name = input("Enter your full name: ").capitalize()

        #---------------
        # this condition exist if ever the pincode rule is followed or not...
        while True:
            #-------------------
            #this condition exist for the purpose of displaying the full_name if already created or not..for situational ready purpose...
            while True:
                if not full_name:
                    break
                else:
                    print("Name: " + full_name)
                    break
            #----------------------
            pincode = input("Enter your pincode \033[3mMUST BE 4 DIGIT/NUMBERS\033[0m: ")

            if not pincode.isdigit() or len(pincode) != 4:
                print("ERROR\nRULES:")
                loading_screen(("\n" * 10) + "1. Pincode must not contain spaces\n2. pincode must be a digit\n3. pincode must be 4 digits",2)
                continue

            else:
                choice = input("Would you like to create this new account? (y/n): ").upper()
                if choice == "Y" or choice == "YES":

                    loading_screen("\ncreating your account...", 1)
                    encrypted = encrypting_nu(pincode, master_key, 'encrypt')

                    create_bank_account(full_name, encrypted)


                    loading_screen("\nSuccessfully created your account...", 0.5)

                    for id_number, details in bank_accounts.items():
                        if details['name'] == full_name:
                            print(f"This is your ID number: {id_number}\nMake sure to save it as you need it to login into the bank vault.")

                    input("Press enter to proceed to login page.")
                    loading_screen("loading....", 1)
                    clear_screen()


                    from main_menu import menu_screen
                    return menu_screen()

                else:

                   break
        #--------------------
        continue
    #-------------------------------------------------------



