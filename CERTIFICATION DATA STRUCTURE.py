def adding(settings, value_pair):
    key, value = value_pair
    key = key.lower()
    value = value.lower()


    if key in settings:
        return f"{key} already exist."


    settings[key] = value
    return f"Succesfully Added"


def view(settings):

    if not settings:
        return "Nothing Exist inside your settings"


    result = ("SETTINGS: ")
    for key,value in settings.items():
        result += f"\n{key.capitalize()} : {value}"

    return result


def delete(settings, key):
    key = key.lower()
    


    if key in settings:
        settings.pop(key)
        return f"{key} sucessfully removed"

    return f"{key} DONT EXIST"


nemp = {}

while True:
    print('[1] Add settings [2] View Settings [3] Delete settings')

    choice = int(input("ACTION: "))
    if choice == 1:
        key = input("KEY: ")
        value = input("Value: ")

        pair = (key, value)

        print(adding(nemp, pair))

    elif choice == 2:

        print(view(nemp))


    elif choice == 3:

        if not nemp:
            print("Nothing exist")
            continue

        print(view(nemp))
        
        banish = input("Which would you like to remove: ")

        
        
        print(delete(nemp,banish))
        

        


















        
