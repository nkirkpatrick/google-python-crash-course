number = 1
while number <= 7:
	print(number, end=" ")
	number += 1

def show_letters(word):
	for x in word:
		print(x)

show_letters("Hello")
# Should print one line per letter

for x in range(1, 10, 3):
    print(x)


for x in range(10):
    for y in range(x):
        print(y)

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

