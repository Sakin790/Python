class Employe:
    companyName= "ZXC"
    def __init__(self, empID=None, name=None, salary=None):
        self.empID = empID
        self.name = name
        self.salary = salary
    def changeName(self,name):
        self.name=name
        return name
    def chnageID(self, id):
        self.id=id
    def increaseSalary(self, salary):
        self.salary=salary
    def getName (self):
        return self.name
    def getID(self):
        return self.empID
    def getSalary(self):
        return self.salary

emp1= Employe(1,"Sakin",25000)
print(emp1.getName())
print(Employe.companyName)
print(emp1.companyName)
print(emp1.changeName("Mahid"))