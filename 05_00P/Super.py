class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return (f"{self.brand} {self.model}")

class Electric(Car):
    def __init__(self, brand, model, battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size

electricCar= Electric("Tesla", 456, "85kwh")

print(electricCar.battery_size)
print(electricCar.full_name())

car1= Car("BMW", "GH54L")
print(car1.brand)
