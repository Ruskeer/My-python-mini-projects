def log(func):
    def wrapper(self, *args, **kwargs):
        print(f"[LOG]: '{self.name}' uses {func.__name__} function")
        return func(self, *args, **kwargs)
    return wrapper




class Game:
    def __init__(self, name):
        self.name = name


    @log
    def move(self, direction):

        print(f"{self.name} has moved to {direction}")

    @log
    def attack(self):
        print(f"{self.name} has swung their sword!")



hero = Game("Betlog")

hero.move("North")

print()

hero.attack()
