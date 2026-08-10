def required_admin(func):
    def wrapper(self, *args, **kwargs):

        if self.role != "admin":
            print(f"{self.name} is denied. Must be an Admin")
            return None

        return func(self, *args, **kwargs)
    return wrapper


class Burat:
    def __init__(self, name, role):
        self.name = name
        self.role = role


    @required_admin
    def database(self):
        print(f"{self.name} with an {self.role} role, has deleted the database")

player1 = Burat("Bilat" ,"player")
admin1 = Burat("Burat", "admin")


player1.database()
admin1.database()
