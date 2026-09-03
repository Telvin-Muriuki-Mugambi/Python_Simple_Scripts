class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def make_sound(self, sound):
        return f"{self.name} says {sound}!"

dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

print(dog.describe())  # Output: Buddy is a 3-year-old Dog.
print(cat.make_sound("Meow"))  # Output: Whiskers says Meow!