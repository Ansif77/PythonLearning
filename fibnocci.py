# def fibinocci(n):
#     #Base Case
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     #Recrusive Case
#     else:
#         return fibinocci(n-1) + fibinocci(n-2)
#     # print function
# print(fibinocci(5))


# print result which is number in 6th position
def fibinocci(n):
    
    #Base Case
    if n==0:
        return 0
    elif n==1:
        return 1
    #Recrusive Case
    else:
        return fibinocci(n-1) + fibinocci(n-2)
    # print function
print(fibinocci(6))
def sum_fibinocci(n):
    if n==0:
        return 0
    else:
        return fibinocci(n) + sum_fibinocci(n-1)
print(sum_fibinocci(6))




#Sum listn
# def sum_list(lst):
     #base case
#     if not lst:
#         return 0
#     #Recursive case
#     else:
#         return lst[0] + sum_list(lst[1:])

# print(sum_list([1,2,3,4,5,6,7,8,9]))