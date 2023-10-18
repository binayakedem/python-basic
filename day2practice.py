# tuple in python

tup=(1,4,5,6)

tup1=(1)# this is act as single integer
# but if you wish to make tuple you just need to put comma(, ) at end i.e.
tup2=(1,)
print(type(tup))

#  this is used when you are trying to use without change in future then you use the tuple alternative to tuple

tup3=("Binaya","Bikash", "Bijaya","Rajesh",23,43)
print(len(tup3))
print(tup3[::-1])
print(tup3[3])

if 22 in tup3:
    print("yes 23 is present in tuple")
else:
    print("the given number is not present in tuple")
    
# set is require to make separate the similar and dissimilar in given set of data

sets={1,2,3,4,23,3}
print(sets)

# this set doesnot provide the ordered
for value in sets:
    print(value)
print(type(sets))

dicts={}
print(type(dicts))


#  this is the dictionary portion

dic={
    "Binaya":"human name",
    "Soap":"Object"
}
print(dic["Soap"])


