# Multiple Inheritance 
# When a class inherits from multiple base classes, it is called multiple inheritance. In this case, the derived class inherits all
# the attributes and methods of the base classes.

#Base class 1

class Animal:
    def __init__(self, name):
        self.name=name

    def speak (self):
        print ("Subclass must implement this method")
    
#Base class 2
class Pet:
    def __init__(self,owner):
        self.owner=owner

#Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

def speak(self):
    print (f"{self.name} say woof")

#create an object
dog1=Dog("Tommy","Krish")
speak(dog1)
print (f"Owner: {dog1.owner}")  # Output: Owner: Krish