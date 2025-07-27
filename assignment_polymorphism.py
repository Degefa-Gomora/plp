# Assignment 1: Design Your Own Class! 🏗️

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}! 💪")
    
    def use_power(self):
        print(f"{self.name} uses {self.power}! ⚡️")


# Inheritance: A specific kind of superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, wingspan):
        super().__init__(name, power, city)
        self.wingspan = wingspan

    def use_power(self):
        print(f"{self.name} flies through the skies with a wingspan of {self.wingspan} meters! 🕊️")


# Creating objects
hero1 = Superhero("NightShadow", "Invisibility", "Gothamia")
hero2 = FlyingSuperhero("SkyWing", "Flight", "Cloudopolis", 15)

# Method calls
hero1.introduce()
hero1.use_power()
print("-----")
hero2.introduce()
hero2.use_power()


# Activity 2: Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

print("\n--- Vehicle Movements ---")
for v in vehicles:
    v.move()
