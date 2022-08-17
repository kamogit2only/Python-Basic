class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age
        
    @property    
    def age(self):
        print("get age is called.")
        return self._age
    
    @age.setter            
    def age(self, age):
        print("set age is called.")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age
            
    #age = property(get_age, set_age)


john = Person("John", 10)
print(john.age)
john.age = -10