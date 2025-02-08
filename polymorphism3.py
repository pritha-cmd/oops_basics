#polymorphism with ABCs (Abstract Base Classes)
#ABCs are classes that cannot be instantiated directly

from abc import ABC, abstractmethod

#define an abstract base class
class Vehicle(ABC):
    #define an abstract method
    @abstractmethod
    def drive_engine(self):
        pass

#derived class 1
class Car(Vehicle):
    def drive_engine(self):
        return "Car engine is running"
    
#derived class 2
class Truck(Vehicle):
    def drive_engine(self):
        return "Truck engine is running"
    
#polymorphism function
def drive_vehicle(vehicle):
    return vehicle.drive_engine()

#creating objects
car = Car()
truck = Truck()

print(drive_vehicle(car))  #output: Car engine is running
print(drive_vehicle(truck))  #output: Truck engine is running
