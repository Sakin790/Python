class student : 
    def __init__(self, name, marks):
        self.name=name
        self.marks= marks
    def getAvg(self):
        sum=0
        for x in self.marks:
            sum+= x 
            print(x/3)


s1= student("Abir", [47,55,88])
s1.getAvg()




class car:
   battery= "HSV52V"
   def __init__(self, Battery, Engine, speed, distance):
   
    self.engine = Engine
    self.speed = speed
    self.distance = distance
  
   def durutto(self):
    return (self.distance/self.speed)
   
   def changeBattery(self,newBattery):
      battery = self.newBattery

car1= car("FK35V", 555, 13, 100)
print(car1.durutto())
print(car1.changeBattery("GD78V"))


#Static Methood
class student :
    collegeName= "BGC"
    def __init__(self, name , marks):
        self.name=name
        self.marks=marks

    def printName(self):
        print(self.name)
    @staticmethod
    def printCollege():
        print(student.collegeName)

s1= student("Sakin", 97)
s1.printName()
s1.printCollege()
