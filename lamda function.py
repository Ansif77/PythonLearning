def add(a,b):
    """This function used to add two number"""
    return a+b
a=add(4,6)
print(add.__doc__)

# lambda function (anonymous function)
add= lambda a,b:a+b
print(add(5,6))

# map 
numbers=[1,2,3,4,5,6]
square=map(lambda a:a**2,numbers)
print(list(square))

# filter 
num=[1,2,3,4,5,6,7,8,9,10]
filtered=filter(lambda x:x%2==0,num)
print(list(filtered))

# reduce
from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]
red=reduce(lambda x,y:x+y,num,0)
print(red)

