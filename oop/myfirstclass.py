class Person:
    
    
    num_legs = 2
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def walk(self):
        print(f"{self.name} is walking.")
        
    def run(self):
        print(f"{self.name} is running.")

john = Person("John", 28, "male")
taro = Person("Tato", 18, "male")
emma = Person("Emma", 40, 'female')

john.walk()
emma.walk()

print(john.num_legs)