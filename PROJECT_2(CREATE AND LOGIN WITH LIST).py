accounts = [{'index' : 0, 'username' : 'unknown', 'password' : 'unknown', 'inventory': [], 'inventory2' : [] }]
master_key = 'practicingasusual'
discarded_accounts = []

def crypt(psw, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index_key = 0
    global master_key
    result = ''

    for char in psw:
        if char.isalpha():
            indexofchar = index_key % len(key)
            showkey = key[indexofchar].lower()
            shift = alphabet.index(showkey)

            indexofpsw = alphabet.index(char.lower())

            if mode == 'encrypt':
                formula = (indexofpsw + shift) % len(alphabet)
            else:
                formula = (indexofpsw - shift) % len(alphabet)

            new_char = alphabet[formula]
            
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char

            index_key += 1
        else:
            result += char
        
    return result
        

def int_rule(text):
    
    user_data = input(text)
    if user_data.isdigit():
        return int(user_data)
    return None
    
def inserting_email(user, passw):

    new_id = len(accounts)

    new_data = {
        'index' : new_id,
        'username' : user,
        'password' : passw,
        'inventory' : [],
        'inventory2' : []
        }

    return new_data

def login():
    max_attempts = 3
    print("---LOGIN---")

    for attempt in range(1, max_attempts + 1):
        user_input = input("Username: ")
        pass_input = input("Password: ")

        found_account = None

        for accs in accounts:
            if accs['username'] == user_input:
                found_account = accs
                break

        if found_account:

            decrypt = crypt(pass_input, master_key, 'encrypt')

            if found_account['password'] == decrypt:
                print("Logging in...")
                return dashboard(found_account)
            else:
                print(f"Wrong password...Attempts : {attempt}")
        else:
            print("Username doesn't exist")
            choice = input("Would you like to create an accounts? Y/N: \n")
            if choice.lower() == 'y':
                return create_account()
            else:
                exit()

    return "Access Denied"

            
def view_inventory(current_user):
    if not current_user['inventory']:
        print("Inventory is empty")
        return dashboard(current_user)
    else:
        for each in current_user['inventory']:
            print(f"Item : {each['item_name']} | Quantity : {each['qty']}")


    return dashboard(current_user)
            
def delete_item(current_user):
    print("---- DELETE AN ITEM ----\n")
    
    if not current_user['inventory']:
        print("Inventory is already empty.")
        return dashboard(current_user)

    # Show them what they have
    for item in current_user['inventory']:
        print(f"- {item['item_name']} ({item['qty']}x)")

    choice = input("\nInput the item name to delete: ").lower()
    
    # We use a flag to keep track if we found it
    found = False
    
    for each in current_user['inventory']:
        if each['item_name'].lower() == choice:
            current_user['inventory'].remove(each)
            print(f"\nSUCCESS: {choice} has been removed.")
            found = True
            break # Stop looking once we find and delete it

    if not found:
        print("\nERROR: Item doesn't exist in your inventory.")
        # Optional: Ask them to try again
        retry = input("Try again? Y/N: ")
        if retry.lower() == 'y':
            return delete_item(current_user)

    return dashboard(current_user)
    

def create_account():
    print("---ACCOUNT CREATION---")
    user = input("Username: ")
    passw = input("Password: ")

    crypting_pass = crypt(passw, master_key, 'encrypt')

    finally_created = inserting_email(user, crypting_pass)
    accounts.append(finally_created)

    print("Account Created..Please login to the page...")
    return login()

def dashboard(main_user):
    print("Welcome to the Dashboard")
    print("[1] Add Item | [2] View Inventory | [3] Edit Quantity of an Item | [4] Delete an item | [5] Logout")
    choice = int_rule("Action: ")

    if choice == 1:
        return adding(main_user)
    elif choice == 2:
        return view_inventory(main_user)
    elif choice == 3:
        return edit_quantity(main_user)
    elif choice == 4:
        return delete_item(main_user)

def adding(current_user):
    print("---Add section---")

    while True:
       
            item = input("Item name: ")
            quantity = input("Quantity: ")
            added = current_user['inventory'].append({'item_name': item, 'qty': quantity})
            print("Succesfully Added")
            choice = input("Do you wanna add more? Y/N: ")
            if choice.lower() == 'y':
                continue
            else:
                return dashboard(current_user)
            
def edit_quantity(current_user):
    if not current_user['inventory']:
        print("There's nothing to edit")
        return dashboard(current_user)
    else:
        
        print("---INVENTORY---")
        for each in current_user['inventory']:
            print(f"Item : {each['item_name']}     |    Quantity : {each['qty']}")

        found_item = None
        choice = input("Enter an item name you would like to edit of its quantity: ")
        for item in current_user['inventory']:
            if item['item_name'].lower() == choice.lower():
                print(f"Item : {item['item_name']} |  Quantity : {item['qty']}")
                found_item = item
                
                edit = int_rule("Enter the new Quantity: ")
                found_item['qty'] = edit
                
                print("Quantity successfully changed")
                return dashboard(current_user)
            else:
                print("You don't have that item...\n")
                return dashboard(current_user)

                

        
            
            
                

    
def main_menu():
    print("[1] Login, [2] Create an account, [3] Exit")
    choice = int_rule("ACTION: ")
    if choice is None:
        print("Must be a digit..\n")
        return main_menu()

    if choice == 1:
        return login()
    elif choice == 2:
        return create_account()
    elif choice == 3:
        exit()
        
    





print("----EMAIL CREATION PRACTICE ----")
main_menu()



    
    
    
