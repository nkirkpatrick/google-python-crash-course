file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,ext))

print(file_counts.keys())

print(file_counts.values())

for value in file_counts.values():
    print(value)

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, item in cool_beasts.items():
    print("{} have {}".format(animal, item))

