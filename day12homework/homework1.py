import os
flag=True
print("Press 1 for create")
print("Press 2 for read")
print("Press 3 for append")
print("Press 4 for override")
print("Press 5 for menu")
print("Press 6 for exit")

while flag:
    print("Please select your choice:")
    choice=int(input(":"))
    if(choice==1):
        print("You choose create function")
        create_file()
        
        
    elif (choice==2):
        print("You choose read function")
    elif (choice==3):
        print("You choose append function")
    elif (choice==4):
        print("You choose override function")
    elif (choice==5):
        print("You choose read function")
    elif (choice==6):
        print("Program is terminated")
        flag=False
        break
    else:
        print("invalid choice input")
        
        
    def create_file():
            f=open("bins.txt",'r')
            print(f)