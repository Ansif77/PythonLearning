def greet(name,age,place):
    print(f"hello {name} you are {age} years old, from {place}")


greet("alice",20,"new york")

# return can store item to a variable 
# def sum(a,b):
#     return a+b

# a=sum(1,5)
# print(a)
# print(a+10)

# position argument
# def greet(name,age,place):
#     print(f"hello {name} you are {age} years old, from {place}")


# greet("alice",20,"new york") 

# keyword argument 
def m(name,age):
    print(f"hello {name} {age} years old")

m(name="alice",age=20) 

# default argument 
def l(name="john",place="palakkad"):
    print(f"{name}")


