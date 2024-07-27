
class Person:
    def __init__(self,firstName,lastName,age,department):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.department=department

class Student(Person):
    
    
    def __init__(self, firstName, lastName, age, department,id):
        super().__init__(firstName, lastName, age, department)
        self.id=id
        self.courses=["Com101","Com201","Com301"]
        self.newCourses=[]

    def getStudentId(self):
        return self.id

    def controlAndAddCourse(self,course):
        if(course in self.courses):
            return f"{course} zaten kurs icinde."
        else:
            self.newCourses.append(course)
            return (f"{course} kursu eklendi.")

    def removeCourse(self,course):
        if course in self.newCourses:
            self.newCourses.remove(course)
            return(f"{course} kursu silinmistir.")
        else:
            return (f"{course} kursu kurslarin icinde yoktur.")

    def getCourses(self):
        return (f"{self.newCourses}")

    def __str__(self):
        return f"Student:{self.firstName} {self.lastName} Age:{self.age} Department:{self.department} Student ID:{self.id} Courses:{self.newCourses}"

class Graduate(Person):
    def __init__(self, firstName, lastName, age, department,graduationYear,gpa):
        super().__init__(firstName, lastName, age, department)
        self.graduationYear=graduationYear
        self.gpa=gpa
    
    def getGraduationyear(self):
        return self.graduationYear

    def getGraduationGpa(self):
        return self.gpa
    
    def __str__(self):
        return f"Graduate:{self.firstName} {self.lastName} Age:{self.age} Department:{self.department} Graduation Year:{self.graduationYear} Gpa:{self.gpa}"
    
class Instructor(Person):
    def __init__(self, firstName, lastName, age, department,branch):
        super().__init__(firstName, lastName, age, department)
        self.branch=branch
    
    def getMainBranch(self):
        return self.branch
    
    def __str__(self):
        return f"Instructor:{self.firstName} {self.lastName} Age:{self.age} Department:{self.department} Branch:{self.branch}"




student1=Student("Ahmet","Yilmaz",20,"Endustri Muhendisligi",12345)
inst1=Instructor("Ayse","Demir",35,"Makine Muhendisligi","Makine Muhendisligi")
grdt1=Graduate("Cem","Kara",25,"Elektrik Muhendisligi",2020,3.5)

print(student1)
print(inst1)
print(grdt1)




        