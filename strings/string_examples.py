answer = "YES"
if answer.lower() == "yes":
    print("yes")

new_answer = " Yes "
print(new_answer.strip())
print(new_answer.lstrip())
print(new_answer.rstrip())
print(new_answer.upper().strip())

print("The number of times e occurs is 4".count("e"))
print("Forest".endswith("rest"))
print("Forest".isnumeric())
print("12345".isnumeric())
print("Forest".isalpha())
print("12345".isalpha())
print(int("12345") + int("54321"))
print(" ".join(["This", "is", "a", "phrase"]))
print("...".join(["This", "is", "a", "phrase"]))
print("This is a phrase".split())
print("This is a string".endswith("g"))




