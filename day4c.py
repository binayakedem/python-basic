#tuples person value and relateion below  (hw)


#start to learn typecasting

#one data type to another data type conversion is called type casting
# pie=3.14
# print(type(pie))
# print(pie)
# print(type(int(pie)))

# value="3.14"
# print(type(value))
# x=float(value)
# print(type(x))
# print(x)

# # you can convert list to tupple

# # hw =list of tuple 

fruits_tuple=('apple','kiwi','grapes')
print(type(fruits_tuple))
for value in fruits_tuple:
    print(value)
    

print("\n\n")
fruits_list=list(fruits_tuple)
fruits_list[2]="Mango"
fruits_tuple=tuple(fruits_list)
print(type(fruits_tuple))
for value in fruits_list:
    print(value)

