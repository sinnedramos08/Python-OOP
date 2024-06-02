class Cat:
    def make_sound(self):
        print("Meow")
    def __str__(self):
        return "Cat"

class Dog:
    def make_sound(self):
        print("Bark")

    def __str__(self):
        return "Dog"

cat1 = Cat()
dog1 = Dog()

for animal in (cat1, dog1):
    print(f"This is from animal {animal}")
    animal.make_sound()
