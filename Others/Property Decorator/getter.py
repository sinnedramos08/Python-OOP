class Circle:
    def __init__(self, radius):
        self._radius = radius #Note that we add single underscore, this is to tell
        #the program that this value will be set to a read only variable

    @property
    def radius(self):
        print("Printing from the Property Method")
        return self._radius 

my_circle = Circle(5)
print(my_circle.radius)  # Calls the getter method
