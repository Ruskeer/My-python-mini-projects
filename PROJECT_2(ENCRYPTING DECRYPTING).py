
master_key = 'sopectible'
vault = {}


def ints(data):
    user_data = input(data)
    if user_data.isdigit():
        return int(user_data)

def process_text(msg, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    result = ''

    for everychar in msg:
        if everychar.isalpha():

            indexofkey = key_index % len(key)
            showkey = key[indexofkey].lower()
            shift = alphabet.index(showkey)

            indexofchar = alphabet.index(everychar.lower())

            if mode == 'encrypt':
                formula = (indexofchar + shift) % len(alphabet)
            else:
                formula = (indexofchar - shift) % len(alphabet)

            new_char = alphabet[formula]

            if everychar.isupper():
                result += everychar.upper()
            else:
                result += everychar

            key_index += 1
        else:
            result += everychar
    return result


print('----Vault----')


while True:
    print("[1] Enter pass | [2] View | [3] Exit")
    choice = ints("Enter number: ")

    if choice == 1:
        site = input("Enter site name: ")
        psw = input("Enter password: ")

        encrypting = process_text(psw, master_key, 'encrypt')

        vault[site] = encrypting

        print("Succesfully Added")
    elif choice == 2:
        if not vault:
            print("Empty")
        else:
            for site, secret in vault.items():

                decrypting = process_text(secret, master_key, 'decrypt')

                print(f"Site:", site, "| Password: ", decrypting)

    elif choice == 3:
        print("Exiting")
        break










        
