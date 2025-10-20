# class Car:
#     def __init__(self,company,model,year,price): #attribute
#         self.company =company
#         self.model = model
#         self.year =year
#         self.price = price

#     def display_info(self): #method
#         return f'{self.company} ,{self.model} ,{self.year} ,{self.price}'
    
# car1= Car('Toyota','Camery','2017','540000')
# print(car1.display_info())
# car2=Car('Ford','Endeavour','2019','125402')
# print(car2.display_info())


# class Iphone:
#     def __init__(self,brand,model,base,price):
#         self.brand = brand
#         self.model = model
#         self.base = base
#         self.price = price

#     def display_info(self):
#         return f'This Phone Made By {self.brand},Latest Model Is {self.model},Its A {self.base} Phone,{self.model} Price Is {self.price}'
    
# phone1=Iphone("Apple",'Iphone 17','Flagship','820000')
# phone2=Iphone("Apple",'Iphone 17 Pro','Flagship','100000')
# phone3=Iphone("Apple",'Iphone 17 Pro Max','Flagship','140000')
# phone4=Iphone("Apple",'Iphone 17 Air','Slim','1250000')

# print(phone1.display_info())
# print(phone2.display_info())
# print(phone3.display_info())
# print(phone4.display_info())

#string method
# class Bike:
#     def __init__(self,brand,make,price):
#         self.brand = brand
#         self.make = make
#         self.price = price

#     def __str__(self):
#         return f'Made by {self.brand},Model {self.make},price {self.price}'
    
# bike1=Bike("Tvs",'Jupiter 125','212552')
# print(bike1)
# print(type(bike1))

# class variable and instance variable 
# class Employee:

#     company="Softronics"  #class variable

#     def __init__(self,name,position):
#         self.name = name            #instance Variables
#         self.position = position    #instance Variables


# emp1=Employee("John","Teacher")
# emp2=Employee("Alice","Student")

# #calling class variable
# print(emp1.company)
# print(emp2.company)

# #calling Instance Variable
# print(emp1.name)
# print(emp2.name)



#Inner Class method
# class Employee:
#     class Company:
#         def __init__(self,cname,location):
#             self.cname = cname
#             self.location = location

#     def __init__(self,name,salary,age,cname,location):
#         self.name = name
#         self.salary = salary
#         self.age = age
#         self.company =Employee.Company(cname,location)

#     def display_employee(self):
#         return f'My Name Is {self.name},{self.age} Years old, I am working in {self.company.cname} at {self.company.location}'
    
# emp1=Employee('JOHN',29000,29,'ABC','PERINTHALMANNA')

# emp1.company.cname='xyz'
# print(emp1.display_employee())


#compotion
# class Company:
#     def __init__(self,cname,location):
#         self.cname = cname
#         self.location = location

# class Employee:
#     def __init__(self,name,age,cname,location):
#         self.name = name
#         self.age= age
#         self.company= Company(cname,location)

#     def display_employee(self):
#         return f'my name is {self.name} {self.age} years old,working in {self.company.cname} at {self.company.location}'
    
# emp=Employee('alice',25,'abc','pattambi')
# print(emp.display_employee())



#tightly coupled
# class Engine:
#     def __init__(self,engine):
#         self.engine = engine

# class Car:
#     def __init__(self,model):
#         self.model= Engine(model)


# car=Car('V6')
# print(car.model.engine)

# del car
# try:
#     print(car.model.engine)
# except NameError as e:
#     print(f'Error:{e}')


#loosely coupled class or  #aggregation
class Company:
    def __init__(self,cname,location):
        self.cname = cname
        self.location = location

class Employee:
    def __init__(self,name,age,company):
        self.name = name
        self.age = age
        self.company = company

    def display_employee(self):
        return f'My Name Is {self.name},I am {self.age} years old,working in {self.company.cname} at {self.company.location}'

c1=Company('ABC','PATTAMBI')
emp=Employee('JOHN','54',c1)
print(emp.display_employee())

del emp
print(c1.cname)
