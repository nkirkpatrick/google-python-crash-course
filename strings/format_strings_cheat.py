# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""


# {:d} integer value
number = 10.5
# number_string = "{:d}".format(number)
#  → '10'

print("Number is {:d} ".format(10))

weather = "Rainfall"

print(weather[:4])
print(weather[::1])
print(weather[::-1])



