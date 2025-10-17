# def fact(n):
# #base case
#     if n==0 or n==1:
#         return 1
#     #Recursive case 
#     else:
#         return n* fact(n-1)
# print(fact(6))

#loop
# def fact(n):
#     a=1

#     for i in range(1,n+1):
#         a=a*i
#     return a

# print(fact(5))


# tail requirement 
def ab(n,accumulator=1):
    if n==0 or n==1:
        return accumulator
    else:
        return ab( n-1, accumulator*n)
    
print(ab(5))