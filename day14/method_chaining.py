class Burger:
    
    def bun(self):
        print("This is dough")
        return self
        
        
    def cheese(self):
        print("This is cheese")
        return self
        
        
    def chicken(self):
        print("This is pepperroni")
        return self
        
        
burger=Burger()
#chaingin method calling
burger.bun().cheese().chicken().bun()