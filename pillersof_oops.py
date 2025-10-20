#encaptualisation

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary

#     def display(self):
#         return f'{self.name},{self.__salary}'
    
#     def update_salary(self,update):
#         self.__salary = update
    
# emp=Employee('john',50000)
# print(emp.display())

# print(emp.name)
# print(emp.__salary)

# emp.update_salary(80000)
# print(emp.display())

# emp.name='bob'
# emp.__salary=60000
# print(emp.name)
# print(emp.__salary)

# print(emp.display())

# class Students:
#     def __init__(self,name,mark):
#         self.name = name 
#         self.mark = mark

#     def grade_mark(self):
#         if self.mark > 90:
#             grade = 'A+'
#         elif self.mark> 80:
#             grade = 'A'
#         elif self.mark > 70:
#             grade= 'B+'
#         else:
#             grade= ' B'
#         return f'{self.name},{self.mark},{grade}'

        
# std1=Students('john',92)
# std2=Students('alice',71)
# print(std1.grade_mark())
# print(std2.grade_mark())



#2
# class Bank:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount<0:
#             print("inavlid amount")
#         else:
#             self.__balance += amount
#             print( f'Deposited {amount}.New balance {self.__balance}')
        
    
#     def withdraw(self,amount):
#         if  self.__balance < amount:
#             print('In sufficient balance')
#         else:
#             self.__balance -= amount
#             print('New balance',self.__balance)

#     def balance(self):
#         print( f'balance is : {self.__balance}')

# p1=Bank('john',0)
# p1.deposit(8000)
# p1.withdraw(900)
# p1.balance()


#single inheritence 

class Animal:
    def __init__(self,name):
        self.name= name

    def speak(self):
        print(f'{self.name} make sound')

class Dog(Animal):
    def speak(self):
        print(f'{self.name} sound Woof!')

d=Dog("Bob")
d.speak()
