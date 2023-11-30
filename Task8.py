# Task1: Create circle class with constructor
class Circle:
    #Task2: Create proper member variable
    __pi = 3.141


    # constructor method
    def __init__(self, radius):
        self.radius = radius


    # Task3: method to calculate Area of a circle
    def AreaCircle(self):
        area = self.__pi * self.radius * self.radius
        return area
   
    # Task3: method to calculate perimeter of a circle
    def PerimeterCircle(self):
        perimeter = 2 * self.__pi * self.radius
        return perimeter

class area_perimeter_circle(Circle):
    pass


c = area_perimeter_circle(20)
print(" Task 8: Print area and perimeter of a circle")
print("")
print("*******************************************")
print((""))

print("Area of circle is: ",c.AreaCircle())
print("")

print("Perimeter of the ciecle is: ",c.PerimeterCircle())

print("")
print("______________________________END OF PROGRAM_________________________________________")
