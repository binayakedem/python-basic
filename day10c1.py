# def number(start=0):
#     print(start)
#     if(start<=20):
#         return
#     number(start+1)
    
# number()
# range() homework
# recursion range
# start, end, pattern


 
# lambda function


def myFunc(n):
    return lambda a:a*n

doubler=myFunc(3)

print(doubler(10))

triple=myFunc(4)
print(triple(10))

