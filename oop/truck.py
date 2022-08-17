from car import Car

class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_capacity)  -> None:
        super().__init__(model_name, mileage, manufacturer)
        self._max_capacity = max_capacity
        self._loadings = 0       
        
    def gas(self):
        if self._loadings > self._max_capacity:
            print("重量オーバーです。出発できません。")
            print(f"{self._loadings - self._max_capacity}t の荷物を降ろしてください。")
        else:
            super().gas()
                
    def load(self, weight):
        if weight > 0:
            # load weight
            print(f"{weight}t の荷物を積みました。")
            self._loadings += weight
        else:
            # unload weight           
            if self._loadings <= -weight:
                print(f"{self._loadings}t 全て荷物を下ろしました。")
                self._loadings = 0
            else:
                # weightは負の値なので符号は”+”になっている。
                self._loadings += weight
        print(f"現在の積載量は{self._loadings}tです。")
        
        if self._loadings > self._max_capacity:
            print(f"最大積載量は{self._max_capacity}t,重量オーバーです。")
            
            
if __name__ == "__main__":            
    isuzu_truck = Truck("Track A", 6, "ISUZU", 10)
    print(isuzu_truck.gas())
    isuzu_truck.load(5)
    isuzu_truck.load(-3)
    isuzu_truck.load(10)
    print(isuzu_truck.gas())
    isuzu_truck.load(-30)

