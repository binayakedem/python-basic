
my_list=['Mango','apple','orange','guava','lemon']

print("To see the lenght of list")
print(len(my_list))
print(my_list)
print("\nTo access list using index")
print(my_list[3])

print("\nTo insert data in list with specific index as 2")
my_list.insert(2,"Lady finger")
print(my_list)

print("\nTo append data in list at end is ")
my_list.append("Mashroom")
print(my_list)

print("\nTo remove specific item from list as ")
my_list.remove("apple")
print(my_list)

print("\nPop is used to remove according to given index but if you haven't provide any index just remove last index data in list")
my_list.pop(2)
print(my_list)

print("\n del is used for delete data or entire list")

del my_list[3]
print(my_list)

print("\n reverse() method is used to reverse the list")
my_list.reverse()
print(my_list)



