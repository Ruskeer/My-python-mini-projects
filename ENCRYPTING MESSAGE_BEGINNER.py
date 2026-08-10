master_key = "Buratskibetlog"
vault = {}

def int_rule(text):
    user_data = input(text)
    if user_data.isdigit():
        return int(user_data)


def pass_vault(password, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    key_index = 0

    for everychar in password:
        if everychar.isalpha():

            indexofkey = key_index % len(key)
            showkey = key[indexofkey].lower()
            shift = alphabet.index(showkey)


            indexofpass = alphabet.index(everychar)

            if mode == 'encrypt':
                formula = (indexofpass + shift) %len(alphabet)
            else:
                formula = (indexofpass - shift) %len(alphabet)

            new_key = alphabet[formula]

            if everychar.isupper():
                result += new_key.upper()
            else:
                result += new_key

            key_index += 1
        else:
            result += everychar
    return result



print('----VAULT----')

while True:
    print('[1] Add password | [2] View | [3] Exit')

    choice = int_rule("ACTION: ")

    if choice == 1:
        site = input("Enter site name: ")
        psw = input("Enter password: ")

        encrypting = pass_vault(psw, master_key, 'encrypt')

        vault[site] = encrypting

        f = open("test.txt", 'a')
        f.write(site + ":" + encrypting + "\n")
        f.close()


    elif choice == 2:
        if not vault:
            print("Vault is empty")
        else:

            print("VAULT: \n")
            for site, secret in vault.items():
                show_pass = pass_vault(secret, master_key, 'decrypt')
                print(f"Site name: {site} | Password :{show_pass}")
    elif choice == 3:
        print("Logging out...")
        break
    
                


        

            
                
