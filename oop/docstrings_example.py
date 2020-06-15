class Piglet:
    """Represents a piglet that can say their name.
    """
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet
        """
        print("Oink! I'm {}!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years.
        """

help(Piglet)

class Person:
    def __init__(self, name):
      self.name = name
    def greeting(self):
        """Outputs a message with the name of the person
        """
        print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

help(to_seconds)


