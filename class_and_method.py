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
class Employee:

    company="Softronics"  #class variable

    def __init__(self,name,position):
        self.name = name            #instance Variables
        self.position = position    #instance Variables


emp1=Employee("John","Teacher")
emp2=Employee("Alice","Student")

#calling class variable
print(emp1.company)
print(emp2.company)

#calling Instance Variable
print(emp1.name)
print(emp2.name)


