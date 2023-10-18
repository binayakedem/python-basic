class Person:
    def __init__(self):
        self.name="Ram"#public
        self._age=12#protected within file it can be access but other file can not handle by importing
        self.__phone=98765# private it will be available within the class
        #if you want to access private variable you can simply define in method and return
    def get_private(self):
        return self.__phone
    #to set private attributes in class simply define function
    def set_private(self,phone_number):
         self.__phone=phone_number
    #to make easy just property is used to call 
    phone_number=property(set_private, get_private)
    
    #using decorate above method will be more easy which is
    # @property #decorate
    # def get_private(self):
    #     return self.__phone
    # @phone_number.setter
    # def set_private(self,phone_number):
    #      self.__phone=phone_number
    
    
    
    
    
    
    
p=Person()
print(p.name)
print(p._age)# this is protected within file it can be access but can not access outside of the file by importing
print(p.get_private()) #phone number is accesss here *private


#to set the class attributes public and protected can set but can not directly private

p.name="Binaya limbu"
print(p.name)

p._age=90
print(p._age)

#to set private attribute
#p.set_private("9876545678")
#to set using property method
#p.phone_number="98767899"
print(p.get_private())