# for a in range(1,10,2):
#     print('*'*a)

# 2
# for b in range(6,1,-1):
#     print('*'*b)

# n=5
# for i in range(n+1):
#     print(' '*(n-i),'*'*(2*i+1))


# n=5
# for a in range(n+1):
#     spaces=' ' * (n-a)
#     stars= '*' * (2 * a - 1)
#     print(spaces+stars)

# row = 5 
# for i in range(4, 0, -1):
#     spaces = ' ' * (row - i)
#     stars = '*' * (2 * i - 1)
    # print(spaces+stars)



a='the cat and the dog'
print('the:',a.count('the'),'cat:',a.count("cat"),'and:',a.count('and'),'dog:',a.count('dog'))


rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()







# highorder function 
def highorder(a,b,subs):
    return subs(a,b)

def plus(a,b):
    return a+b

def multiply(a,b):
    return a*b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

print(highorder(2,5,plus))
print(highorder(5,4,multiply))
print(highorder(100,10,division))
print(highorder(10,5,substraction))