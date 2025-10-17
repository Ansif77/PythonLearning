# create a dictionary 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# print(d)

# create dictionary another method 
# another_dic=dict(name="ansif",age="18",place="palakkad")
# print(another_dic)

# access a dictionary value by key 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# print(d["name"])

# access by get tag 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# print(d.get("name"))

# change value in dict 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# d["age"]=20
# print(d)

# add a new item into dict 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# d["pin"]=123456
# print(d)


# clear a dictionary 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# d.clear()
# print(d)

# pop dictionary 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# d.pop("age")
# print(d)

# popitem a dictionary remove last item in the dict
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# d.popitem()
# print(d)

# delete dict 
# d={
#     "name":"ansif",
#     "age":"18",
#     "place":"palakkad"
#     }
# del d["age"]
# print(d)

# create nested dict 
# nested_dict={
#     "person1":{"name":"john","age":"20"},
#     "person2":{"name":"boby","age":"30"}
# }
# print(nested_dict["person1"]["name"])

# change value 
# nested_dict={
#     "person1":{"name":"john","age":"20"},
#     "person2":{"name":"boby","age":"30"}
# }
# nested_dict["person1"]["age"]="50"
# print(nested_dict)

# add value 
# nested_dict={
#     "person1":{"name":"john","age":"20"},
#     "person2":{"name":"boby","age":"30"}
# }
# nested_dict["person2"]["country"]="poland"
# print(nested_dict)


# calling keys 
# data={"name":"ansif","age":"18"}
# print(data.keys())

# caling values 
# data={"name":"ansif","age":"18"}
# print(data.values())

# calling keys values separately 
# data={"name":"ansif","age":"18"}
# print(data.items())

# update dict 
# data={"name":"ansif","age":"18"}
# data.update({"city":"new york"})
# print(data)

# set default 
# data={"name":"ansif","age":"18"}
# s=data.setdefault("city","newyork")
# print(data)

# set values default                   false code
# data={"name","age"}
# nd=data.fromkeys(data,"new york")
# print(data)