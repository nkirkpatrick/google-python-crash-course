
import os
import sys


print(sys.version)
print(sys.executable)

name = input("Your name: ")
print("Hello, ", name)

def first_and_last(message):
    if len(message) == 0 or (str(message[0]) == str(message[-1])):
        return True
    else:
        return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last("Norbert"))
print(first_and_last(""))
