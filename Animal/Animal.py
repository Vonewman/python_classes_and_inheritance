class Animal(object):


    def __init__(self, name):
        self.name = name
    def eat(self,food):          # Common method(or property)
        print("%s is eating %s. " % (self.name, food))

class Dog(Animal):

    def fetch(self, thing):
        print("%s goes after the %s!" %(self.name, thing))

class Cat(Animal):

    def swatstring(self):
        print("%s shreds the string!" %(self.name))


d = Dog('Ranger')    # Created Dog object
c = Cat('MeOw')      # Created Cat object

d.fetch('ball')
c.swatstring()
d.eat('Dog Food')
c.eat('Cat Food')
#d.swatstring() 