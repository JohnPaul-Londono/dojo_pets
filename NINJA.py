from pet import Pet, Cat

class Ninja(Pet):
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print("Walking Pet")
        return self

    def feed(self):
        self.pet.eat()
        print("Feeding Pet")
        return self
    
    def bathe(self):
        self.pet.sound()
        print("Washing Pet")
        return self

steve = Ninja("Steve","Patt", Cat("Bumi", "Crazy Boy", 50, 100),"Anything","Wet")
john = Ninja("John", "London", Cat("Kya", "RUN", 100, 50), "Crunchies", "Dry")

print(steve.pet.name)
print(steve.pet.health)
print(steve.pet.trick)
steve.walk()
print(steve.pet.health)
steve.feed()
print(steve.pet.health)
steve.bathe()
print(steve.pet.health)

print(john.pet.name)
print(john.pet.health)
print(john.pet.name)
john.walk()
print(john.pet.health)
john.feed()
print(john.treats)
print(john.pet.health)
john.bathe()
print(john.pet.health)



