class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    
my_circle = Circle(5)
print(my_circle.radius)  # Output: 5
my_circle.radius = 7  # Calls the setter method
print(my_circle.radius)  # Output: 7
