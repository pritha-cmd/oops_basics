#polymorphism with functions and methods

# base class
class Shape:
    def area(self):
        return "the area of the figure"
    
#derived class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
#function that demonstrates polymorphism
def calculate_area(shape):
    return shape.area()

#creating object 
rectangle=Rectangle(4,5)
circle=Circle(3)
print(calculate_area(rectangle)) #output: 20
print(calculate_area(circle)) #output: 28.26
