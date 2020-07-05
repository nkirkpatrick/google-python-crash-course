punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string = "test%%%"
valid_word = True
new_string = " "

for letter in string:
    print(letter)
    if letter in punctuations or letter.isalpha():
        print("true")
        valid_word = True
    else:
        valid_word = False
        break
if valid_word:
    new_string = string

print(new_string)
print(valid_word)