# try:
#     with open("output.txt", "w") as file:
#         file.write("Hello World")
#     print("File written successfully!")
# except PermissionError:
#     print("Permission denied!")




    
def most(str):
    a=sorted(str)
    count=0
    prev=a[0]
    dish={}
    for i in a:
        if i == prev:
            print(i)
            print(prev)
            count+=1
            prev=i
        else:
            dish[prev]=count
            count=0
    return dish

print(most("aabb"))