class student: 

    schoolName = "Solua High School"
    def __init__(self,name, dept, marks,city):
        self.name = name
        self.dept = dept
        self.marks = marks
        self.city = city

    def getStudentDetails(self):
        return (f"This is {self.name} from {self.dept}, he got {self.marks} marks. he is from {self.city}")
    
    @staticmethod
    def getStudentSchool():
        return student.schoolName
    
s1= student("Sakin", "science", 87, "Rajshahi")

print(s1.getStudentDetails())
print(student.getStudentSchool()) #Without creating Object, Static methood
print(s1.getStudentSchool())