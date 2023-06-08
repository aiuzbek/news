# inheritance -> meros

# class Car:
#     def __init__(self,name,brand,color):
#         self.name = name
#         self.brand = brand
#         self.color = color
        

# car = Car('Bugate','bugate','white')
# car2 = Car('nexia3','Chevrolet','malochniy')
# c = Car('Malebu','chev','black')
# print(car.name)
# print(car2.name,car2.color)
class Parent:
    def __init__(self,name,familya,age,gender,money):
        self.name = name
        self.familya= familya
        self.age = age
        self.gender = gender
        self.money = money
    def get_info(self):
        return f"My name is {self.name}"
    
class Student(Parent):
    def __init__(self, name, familya, age, gender, money,kurs):
        super().__init__(familya,name,age,gender,money)
        self.kurs = kurs
    def get_info(self):
        return f"Hello bollaik happy children day"
    def get_kurs(self):
        return f""
         
class Uqitivchi(Parent):
    pass
 
class Dasturchi(Parent):
    pass

student = Student('Ahmad',"Qilichiv",18,"male",'1mln$','3-kurs') 
print(student.get_info(),student.kurs)
        
