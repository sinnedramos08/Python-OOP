class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self):
        print("Deleting the circle")
        del self._radius

my_circle = Circle(5)
del my_circle.radius  # Calls the deleter method
