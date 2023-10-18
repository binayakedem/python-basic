my_fruit_list=[]
flag=True
print("Press '0' for exit ")
print("Press '1' for display fruits")
print("Press '2' for Menus")
print("Other wise just enter fruit name")
while flag:
    fruit=input("Enter a fruit name:")
    if fruit=="0":
        flag=False
    elif fruit=="1":
        print("\nList of fruits are:")
        for fruts in my_fruit_list:
            print(fruts)
    elif fruit=="2":
        print("See the Menus\n")
        print("Press '0' for exit ")
        print("Press '1' for display fruits")
        print("Press '2' for Menus")
        print("Other wise just enter fruit name")
    else:
        my_fruit_list.append(fruit)
        
        
        
