strin=" This is Binaya limbu {}"
# you can access the string from anywhere i.e.

print(strin[2])

# slicing in string start from 0 and ending with -1 i.e.
print(strin[:-1])
print(strin[8:15])
# to convert above into uppercase is

print(strin.upper())
# to convert into lowercase is
print(strin.lower())
print(len(strin))
# to remove the white space
print(strin.strip())
print(len(strin))

# replace function is used to replace character

print(strin.replace("Binaya","Bikram"))

# you can split the sentence into different word 
print(strin.split(" "))

# format function in python

age=34
print(strin,age)
print(strin.format(age))

