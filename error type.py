# a=[mjjshhs]
# print(a)


#index error
# a=[1,2,3]
# print(a[4])

#type error
# def ab(ss):
#     print("eee")
# ab()

#key error
# dic={
#     "a":"10",
#     "b":"20"
# }
# print(dic["h"])

# value error 
# int("hello")

#file not found 
# file=open("zz.txt","r")
# print(file)


# ZeroDivisionError 
# d=(10/0)
# print(d)


try:
    x=10/0
except ZeroDivisionError:
    print("you can't divide by zero")