class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

def drive (self):
    print(f"the person will drive {self.enginetype} car")

car1= Car(4,5,"petrol")
drive(car1)

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving=is_selfdriving

def selfdriving(self):
    print(f"Tesla supports self driving : {self.is_selfdriving}")
    
tesla1=Tesla(4,5,"electric", True)
selfdriving(tesla1)
drive(tesla1)


