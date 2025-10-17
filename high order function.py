# do java script task 
def add(n):
    return lambda x:x+n
addten= add(1)
print(addten(5))



# a=10 #gloal scope
# def outer_fun(): #its a nested function 
#     a=5 #Enclosing Scope
#     def inner_fun():
#         a=2 #Local Scope
#         print(a) #Output 2
#     inner_fun()
# outer_fun()
# print(a) #Output 10
# # keep indendation correctly 

