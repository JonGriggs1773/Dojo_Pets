class Pet:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.energy += 25
        return f"Energy Level: {self.energy}"
    def eat(self):
        self.energy += 5
        self.health += 10
        return f"Health and Energy Level are {self.health}, and {self.energy}"
    def play(self):
        self.health += 5
        return f"Health: {self.health}"
    def noise(self):
        print("WOOF!!!")

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks)
