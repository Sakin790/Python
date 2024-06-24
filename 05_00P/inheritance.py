class Car :
    @staticmethod
    def start():
        print("Car Has Started...")
    @staticmethod
    def stop():
        print("Car Stoped...")

class newCar(Car):
    def __init__(self, name):
        self.name= name

car1 = newCar("Farari")
print(car1.name)
print(car1.start())
print(car1.stop())



#Might Have Error
class father :
    height= 6
    def __init__(self, fatherName,):
        self.name = fatherName
    
    @staticmethod
    def mood():
       print("Soo Angry...")

class son(father):
   def __init__(self, name):
       self.name= name

s2=father("Baba")
s1=son("Sakin")
print(s1.name)
print(s1.mood())
print(s1.height)
print(s1.fatherName)
