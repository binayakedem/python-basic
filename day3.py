
# #  this is the tuple and is used when values are not changeable
# my_tuple=(1, "Binaya Limbu",1.222,
#           [1,2,3,4],
#           ('test',134)
#           )
# print(my_tuple)
# for values in my_tuple:
#     print(values)

# print(type(my_tuple))

# print("after")
# #  this prints the last 4 indexed value 

# #  4 represents the index number and and can be access to that tuple with their indexing like 0 ,1 
# print(my_tuple[4][1])


# #  now set in python

# # unordered and mutable , duplicate is not allow in set
# # supports only integer , tuple
# my_set={
#     1,2,3,4,5,6,7,8,1,2,3,4,5,6,"Binaya"
# }

# print(type(my_set))
# print(my_set)
# for value in my_set:
#     print(value)



# # now dictionary

# # mutable , unodered, duplicate is not allow, 

# my_dict={
#     "id":"12",
#     "name":"Binaya Limbu",
#     # "name":"Radha rai",  Binaya Limbu is replaced by Radha Rai
#     "Address":"Kathmandu",
#     "education":"Bachelor running",
#     "marks":[1,2,"this is list ",4]
# }

# print(type(my_dict))

# print(my_dict["name"])
# print(my_dict["marks"][2])
# print(my_dict["marks"][2][::-1])
# # when use dictionary is 

persons=[{
    "name":"binaya Limbu",
    "gender":"male",
    "age":12,
    "address":"kathmandu",
    "phone":"98988623862",
    "language":[
        "python","java", "c++"
    ]   
},{
 "name":"Bijaya Limbu",
    "gender":"male",
    "age":90,
    "address":"Jhapa",
    "phone":"98988623862",
    "language":[
        "C","java", "c++"
    ]
    
    
},
{
 "name":"Bikram Limbu",
    "gender":"male",
    "age":33,
    "address":"Morang",
    "phone":"98988623862",
    "language":[
        "advance java","java", "c++"
    ]
    
    
},
{
 "name":"Bijay Limbu",
    "gender":"male",
    "age":33,
    "address":"Chitwan",
    "phone":"98988623862",
    "language":[
        "Java","advance java", "c++"
    ]
    
    
},
{
 "name":"Binod Limbu",
    "gender":"male",
    "age":44,
    "address":"Palpa",
    "phone":"98988623862",
    "language":[
        "Php","java", "c++"
    ]
    
    
},
{
 "name":"Bikash Limbu",
    "gender":"male",
    "age":32,
    "address":"Ilam",
    "phone":"98988623862",
    "language":[
        "Android developer","java", "c++"
    ]
    
    
},
]
# ctrl+d

print(f"\nYour detail is\n Your name is {persons[0]['name']} and  age is {persons[0]['age']}. You have  learnt programming languages are \n 1.{persons[0]['language'][0]} \n2.{persons[0]['language'][1]}\n3.{persons[0]['language'][2]} ")
print(f"\nYour detail is\n Your name is {persons[1]['name']} and  age is {persons[1]['age']}. You have  learnt programming languages are \n 1.{persons[1]['language'][0]} \n2.{persons[1]['language'][0]}\n3.{persons[1]['language'][2]} ")
print(f"\nYour detail is\n Your name is {persons[2]['name']} and  age is {persons[2]['age']}. You have  learnt programming languages are \n 1.{persons[2]['language'][0]} \n2.{persons[2]['language'][0]}\n3.{persons[2]['language'][2]} ")
print(f"\nYour detail is\n Your name is {persons[3]['name']} and  age is {persons[3]['age']}. You have  learnt programming languages are \n 1.{persons[3]['language'][0]} \n2.{persons[3]['language'][0]}\n3.{persons[3]['language'][2]} ")
print(f"\nYour detail is\n Your name is {persons[4]['name']} and  age is {persons[4]['age']}. You have  learnt programming languages are \n 1.{persons[4]['language'][0]} \n2.{persons[4]['language'][0]}\n3.{persons[4]['language'][2]} ")
print(f"\nYour detail is\n Your name is {persons[5]['name']} and  age is {persons[5]['age']}. You have  learnt programming languages are \n 1.{persons[5]['language'][0]} \n2.{persons[5]['language'][0]}\n3.{persons[5]['language'][2]} ")


