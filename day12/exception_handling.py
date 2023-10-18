
while True:
    try:
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        print(a<b)
        if a<20:
            raise Exception("Custom exception is throwing from here ")
        print(a/b)
    except ZeroDivisionError:
        print("number can not be divided by 0")
    except ValueError:
        print("Invalid inputs")
    except:
        print("Something input is wrong")


