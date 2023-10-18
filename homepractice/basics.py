# to print in screen just use print method
print("This is print function to print the values:")
# variable declaration in python
var=34
# to check type of variable

# to provide multiple line comments simply you can use tripple quotation


""""this is comment part
int ptath and cand not pa"""
print("""
      this can help you to print in
      multiple line but double quotation can give you only on line""")
print(type(var))
print(f"the value is :{var}")


# in python override the value as well
x="Binaya"
print(x)
print(type(x))
x=34#here the x values is override with integer
print(type(x))
print(x)

# in python or any language there are three types of declaration i.e. camel case , pscal case and snake case

my_var="This is the snake case declaration"
print(my_var)
MyVar="This is the pascal case declaration"
print(MyVar)
myVar="this is the cammel case declaration"
print(myVar)

# one of the most important part in python is that multiple variable can be initialized at one line i.e.
a,b,c=23,"Binaya",343
print(a)
print(b)
print(c)
a="orange"
b="Apple"
c="Mango"
print(a+b+c)
print(a,b,c)


# very important thing is that in python separating by comma is more reliable than that of + sign



# python also provide the global varible which can be used in any place 
x="This is Binaya Limbu from Taplejung"
def my_funtion():
    print("This is value from global variable:",x)

my_funtion()

# in some case you can simply use keyword as global to declara variable have globle scope

def my_funtion1():
    global var
    var="This is also become the global variable"

my_funtion1()

print("Inside funtion1 there is global variabe and its value is:",var)

# data types in python= string, int, float , complex, list , tuple , range, dict, set , frozenset, bool, bytes , bytearray, memeoryview, nonetypoe,

x=1j
print(type(x))
print(x)

my_fruits=['Apple','Mango','Guava','Orange','Avagado']

for x in my_fruits:
    print(x)
x=list(range(1,34,3))
print(x)

# sometime random value or number is require in this case python has random to generate random function

# first of all you have to import from random
import random
print(random.randrange(2,100))

# for flexibility string slicing


y="This is the first program ever to slice the overall sentence"

print(y[2:])




