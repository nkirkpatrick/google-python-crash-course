def group_list(group, users):
    members = []
    members.append(group)
    new_members = group + ": "
    user_count = 0

    for uname in users:
        members.append(uname)
        user_count += 1
        if user_count != len(users):
            new_members += uname + ", "
        else:
            new_members += uname

    return new_members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"