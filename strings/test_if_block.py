name = "Norbert"
if name.isalpha():
   print("True")
   print("Name is: " + str(name))

def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        if letter != " ":
            new_string = new_string + letter.lower()
            print(new_string)
    reverse_string = new_string[::-1]
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

