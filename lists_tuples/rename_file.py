filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []

for fname in filenames:
    if fname.endswith(".hpp"):
        index = fname.index(".hpp")
        new_fname = fname[:index] + ".h"
        newfilenames.append(new_fname)
    else:
        newfilenames.append(fname)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
