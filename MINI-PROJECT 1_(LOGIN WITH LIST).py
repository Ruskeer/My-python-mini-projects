my_list = ["apple", "banana"]

def system_vault():

        user = "admin"
        pincode = "1234"

        max_attempts = 3
        global my_list

        def checker(u, p):
                if u == user and p == pincode:
                        return True
                return False

        def listing(text):
                return text.strip().lower()

        def data(att):
                user_data = input(att)
                if user_data.isdigit():
                        return int(user_data)
                return None
        def choice(ad):
                if ad == "Add":
                        maxatt = data("Enter how many items you are going to put in: ")


                        if maxatt is None:
                                return "Must be a number."

                        for item in range(1, maxatt + 1):
                                itemslist = input(f"Item no.{item}: ")
                                clean = listing(itemslist)
                                my_list.append(clean)

                        return f"Your current item in the list {my_list}."
                                
                        
                elif ad == "View":
                        return f"Current items: {my_list}"


                else:
                        return "Invalid input"
                        
                        

        
        print("Welcome! Please login.")
        for attempt in range(1, max_attempts + 1):
                u = input("Username: ")
                p = input("Password: ")
                if checker(u, p):
                        print("ACCESS GRANTED")
                        u_input = input("What do you wanna do with your list? Add or View: ")
                       

                        return choice(u_input)
                            
                              

                else:
                        print("Wrong credentials")


        return "Access denied"



print(system_vault())
