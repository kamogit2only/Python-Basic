class Myclass():
    
    def mymethod(self):
        print("This is normal method.")
        
    @staticmethod
    def mystaticmethod():
        print("This is staticmethod.")
        
        
c = Myclass()
c.mymethod()
Myclass.mystaticmethod()