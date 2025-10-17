# create set 
# a={1,2,3}
# print(a)

# create empty set 
# a=set()
# print(type(a))

# add single item to set
# a={1,2,3}
# a.add(5)
# print(a)

# add multiple item in set 
# a={1,2,3}
# a.update([4,5,6])
# print(a)

# a={"mango","cherry","apple"}
# print("mango" in a)

# for loop 
# a={"mango","cherry","apple"}
# for item in a:
#     print(item)


# remove item in set 
# a={1,2,3,4,5,6}
# a.remove(2)
# print(a)

# discard a item in set 
# a={1,2,3,4,5,6}
# a.discard(7)
# print(a)

# pop a item in set but not support index values 
# a={1,2,3,4,5,6}
# b=a.pop()
# print(a)

# clear items in set 
# a={1,2,3,4,5,6}
# a.clear()
# print(a)


# inter section method print items that items in both sets
# a={1,2}
# a1={1,2,3,4}
# result=a & a1
# print(result)

# - method 
a={1,2}
a1={1,2,3,4}
result=a1 - a
print(result)

# ^ method 
a={1,2}
a1={1,2,3,4}
result=a ^ a1
print(result)

a={1,2}
a1={1,2,3,4}
print(a.issubset(a1))

a={1,2}
a1={1,2,3,4}
print(a.issuperset(a1))