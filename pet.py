class Pet:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def sound(self):
        print(self.noise)
        return self


class Cat(Pet):
    def __init__(self, name, trick, health, energy):
        super().__init__(name, health, energy)
        self.noise = "Meow"
        self.trick = trick













# kya = Pet("Kya","Cat","Be Pretty")
# bumi = Pet("Bumi", "Cat", "Crazy Boy" )

# # print(kya.name)
# # print(kya.animal)
# # print(kya.trick)
# # print(bumi.name)
# # print(bumi.animal)
# # print(bumi.trick)

# print(kya.health)
# kya.eat()
# print(kya.health)

# print(bumi.noise)