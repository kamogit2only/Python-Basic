class Car(object):
    
    
    def __init__(self, model_name, mileage, manufacturer) -> None:
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer
        pass
    
    def gas(self):
        print("{0.manufacturer}, {0.model_name}(mileage:{0.mileage}) gas!".format(self))
        
    def brakes(self):
        print("{0.manufacturer}, {0.model_name}(mileage:{0.mileage}) brakeing!".format(self))
    

if __name__ == "__main__":
    prius = Car("Prius", 20, "TOYOTA")
    print(prius.mileage)
    prius.gas()