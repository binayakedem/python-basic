# range function

# range=datatype

# print(list(range(10)))
# # print(list(range(10)))
# for i in range(0,9):
#     print(i)
# for i in range(0,9,2): #gap=2 initial=0 and range=9
#     print(i)
# print(type(range(10)))

# for i in range(0,10,2):
#     print(i)


# function=reusable block of code is wrap to use in anywhere you can pass parameter, keyword=def


# def hello_world():#parameter
#     print("hello world")
#     print("Valus is")
    
# hello_world()
# hello_world()
# hello_world()
# hello_world()
# hello_world()
# hello_world()

# def hello_world(name):#parameter
#     print(f"hello {name}")
   
    
# hello_world("Rameswor")
# hello_world("Binaya")


# create functiaon name as person 


# def hello_world(name, location, gender, age):#parameter
#     print(f"hello {name} your location is {location} and your gender is {gender}, age={age}")   
# hello_world("Rameswor" age=90, gender=male, location=ranipokhari)


# def person(name, age , location,college, hobbies=()):
#     print(f"My name is {name} and my age is {age}. I am currently live in {location}. My college name is {college} my hobbies are")
#     for hobby in hobbies:
#         print(hobby)
    
# person("Binaya", 26, "Kathmandu", "Orchid international college",hobbies=("football","basketball") )#in this case you directly use the keyword to point hobbies 
    


# multiple attributes you can use args
# def numbers(*numbers):
#     print(numbers)#converts in tuple
# numbers(1,2,3,5,"Binaya")# simply store in tuple


# def person(*names):
#     for name in names:
#         print(name)
        
# person("Binaya","Bikash","Bijay","Binod",8997)

# keyword arguments is require in this case kwargs is used and store in dictionary

# def person(**person):
#     print(f" name is {person['name']} and gender is {person['gender']}, your age is :{person['age']}")
    
        
# person(name="Binaya",gender="Bikash",age=8997)


# make calcutlator as homework
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
print("- for subtraction")
print("+ for Addition")
print("/ for Division")
print("*  for multiplication")
print("0 to terminate")
user_inp=input("Enter your choice:")

if(user_inp=="+"):
    result=num1+num2
    print(f'The sum is: {result}')
elif(user_inp=="-"):
     result=num1-num2
     print(f'The Subtraction is: {result}')
     
elif(user_inp=="*"):
     result=num1*num2
     print(f'The Multiplication is: {result}')

elif(user_inp=="/"):
     result=num1/num2
     print(f'The Division is: {result}')
else:
    print("Wrong choice")
  
    



