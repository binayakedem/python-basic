my_set = {"apple", "banana", "cherry","Papaya","Guava","mango"}
print("first set elements")
print(my_set)

# len() method is used for counting the length of set
print("first element length")
print(len(my_set))

# to add elements in set just use add() method
print("Adding an orange to first set")
my_set.add("Orange")
print(my_set)

# update is used to update the set if same element is given then element is not added to set
print("first and second set are updated")
my_set2={"chicken","Pork","beef","cherry"}
my_set.update(my_set2)
print(my_set)

print("removing chicken from second set")
# remove() method is used to remove particular element in the set
my_set2.remove("chicken")
print(my_set2)

# pop() method is also used but which element is remove can not determine because set is unordered
print("Poping randon element from second set")
my_set2.pop()
print(my_set2)


# intersection,union same as c.math

my_set3={"potato","banana","cherry"}
my_set4={"potato","mango","apple"}
print("intersection between third and fourth sed")
print(my_set4.intersection(my_set3))

