def skip_elements(elements):

    new_list = []
    i = 0
    y = 0

    # Skip every other element in current list and write to new list
    # 
    for i in elements:
        if y % 2 == 0:
            new_list.append(i)
        y += 1
        
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []



