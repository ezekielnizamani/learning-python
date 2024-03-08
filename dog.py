
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever(Dog):
    def speak(self,sound='Bark'):
        return super().speak(sound)
    
miles_golden_dog = GoldenRetriever('miles',4)
print(miles_golden_dog.speak())
# miles = Dog('Miles',4)
# buddy = Dog('Buddy',5)

# print(miles.name)
# print(miles.age)
# print(miles.species)

# print(buddy.name)
# print(buddy.age)
# print(buddy.species)

# buddy.age =10
# print(buddy.age)

# miles.species ='Felis silvestris'
# print(miles.species)

# print(buddy.description())
# print(buddy.speak('You are great'))

# print(miles)