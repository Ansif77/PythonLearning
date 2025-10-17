def a(**kwargs):
    for key , value in kwargs.items():
        print(f'{key}:{value}')
    
a(name="Alice", age=30, city="New York") 

# def abc(**kwargs):
#     return f'my name is {kwargs['name']}, iam {kwargs['age']} years old'

# print(abc(name='ansif',age='20'))

# def abc(**kwargs):
#     print(kwargs)
# abc(name='anshif',age='18',place='palakkad')


# arbitery and keyword argument together 
# first prioriity to aribitery
# def info(*arb,**key):
#     print('Arbitery Argument',arb)
#     print('Keyword Argument',key)

# info(1,2,3,name='john',age='18')

# normal parameter ,arbitery and keyword argument together 
# in this firstt priority is normal parameter the arb,then keyword
# def info(abc,*arb,**key):
#     print('parameter',abc)
#     print('Arbitery Argument',arb)
#     print('Keyword Argument',key)

# info(1,2,3,name='john',age='18')