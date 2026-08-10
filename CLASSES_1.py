class database:
    def __init__(self):

        self.inventory = {}

    

    def add(self, itemname, quantity):

        self.inventory[itemname] = quantity
        print(f"{itemname} has been succesfully added")


    def __contains__(self, item):
        return item in self.inventory

    def __str__(self):

        output = "\n --FINAL INVENTORY ---\n"
        for item, quantity in self.inventory.items():
            output += f"{item} : {quantity}x\n"

        return output



db = database()

while True:

    itemname = input("Enter an item you want to add: ").capitalize()

    if itemname in db.inventory:
        print(f"{itemname} already exists in the database")

        print()
        choice = input("Would you like to overwrite it? y/n : ").lower()

        if choice == "n":
            continue
        else:
            pass

    itemquantity = int(input("Enter quantity of an item: "))

    db.add(itemname,itemquantity)

    choice1 = input("Would you like to add more? y/n : ").lower()

    if choice1 == "n":
        break
    else:
        pass


print(db)












        
    
    
