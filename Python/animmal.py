class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
    def run(self):
        self.health -= 5
    def displayHealth(self):
        print self.name, "HP:", self.health
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 150
    def pet(self):
        self.health += 5
class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I AM A DRAGON"
    def fly(self):
        self.health -= 10
drag1 = Dragon("Drag")
dog1 = Dog("Doggo")
animal1 = Animal("The Thing")
drag1.displayHealth()
dog1.displayHealth()
animal1.displayHealth()
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.displayHealth()
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.displayHealth()
drag1.fly()
drag1.displayHealth()
