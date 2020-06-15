class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name))
        

# Create a new instance with a name of your choice
some_person = Person("Norbert")
# Call the greeting method
print(some_person.greeting())
