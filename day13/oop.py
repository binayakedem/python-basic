class House:
    color="Red"
    garden=True
    window=90
    def __init__(self,color,garden, window):
        self.color=color
        self.garden=garden
        self.window=window
        
    def set_color(self,colors,windows):
        self.color=colors
        self.window=windows


#to call constructor
house_obj3=House("Blue",False,"999")
#constructor is used to initial
house_obj=House()
print(house_obj.color)
#
# another obj of House()
house_obj1=House()
# to call function
house_obj1.set_color("Green",1000)
# capital is class
print(house_obj1.window)
print(house_obj1.color)
print(type(house_obj1.color))# this returns strings
print(type(house_obj1))

