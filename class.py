# classlar
# student = {
#     'name':'Ali',
#     'age':23
# }
# student2 = {
#     'name':'Zamir',
#     'age':12
# }

# gisht = {
#     'ulchami':'300X400',
#     'naxi':5000
# }
# gisht1 = {
#     'ulchami':'400X300',
#     'narxi':6000
# }
class Student:
    def __init__(self,name,familya,age,kurs):
        self.name = name
        self.familya = familya
        self.age = age
        self.kurs = kurs
        self.kim = 'student'
    # method
    def get_info(self):
        return f"Menign ismim {self.name} mening familyam {self.familya} mening yoshim"
        
    
    def __str__(self):
        return f"{self.name}"

student = Student("Zarina",'Axmidova',18,2)
print(student.get_info())

# Car name brand color year speed


