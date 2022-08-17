import time

class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
       
    @classmethod
    def create_form_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year -((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age) 
        
john = Person("John", 20)
emma = Person.create_form_dob("Emma", 1989, 4, 3)
print(emma.age)