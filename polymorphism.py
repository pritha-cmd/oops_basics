#base class
class Animal:
    def speak(self):
        return "Sound of the Animal"

#derived class
class Dog(Animal):
    def speak(self):
        return "Woof Woof"

#derived class
class Cat(Animal):
    def speak(self):
        return "Meow Meow"


dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

#function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)

