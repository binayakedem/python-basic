my_fruits=['apple','mango','guava','orange']
print(len(my_fruits))
for fruits in my_fruits:
    print(fruits)
my_fruits[3]="banana"
for fruits in my_fruits:
    print(fruits)




#  your project is in dictionary you have to collect the data of user name and password in infinite untile user say its enough

detail=[]
print("press 0 for exit")
print("press 1 for insert")
print("press 2 for display")
flag=True

while flag:
    user_name=input("Please enter user name:")
    user_password=input("Please enter user password:")
    choice=int(input("Please enter your choice:"))
    details={
        "username":user_name,
        "userpassword":user_password
    }
    if choice==0:
        flag=False
    elif choice==1:
        detail.append(details)
        
    elif choice==2:
        for x in detail:
            print(list(x))
    else:
        print("Wrong choice")