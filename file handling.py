#CHANGE FILE PATH

# file=open("C:/Users/pc/OneDrive/Desktop/all files/sample.txt","w")
# file.close()


# READ MODE READ THE ENTIRE FILE

# file=open("sample.txt","r")
# con=file.read()
# print(con)
# file.close()

#READLINE read lines 

# file=open("sample.txt","r")
# line1=file.readline()
# print(line1)
# line2=file.readline()
# print(line2)
# file.close()

#readline forloop
#READLINE read lines 

# file=open("sample.txt","r")
# for line in file:
#     print(line)
# file.close()


#strip remove whitespace

# file=open("sample.txt","r")
# for line in file:
#     print(line.strip()) #strip is used to remove whitespaces
# file.close()



#READLINES reads all lines in a file and returns them as a list of strings. 

# file=open("sample.txt","r")
# cont=file.readlines()
# print(cont)
# file.close()

##########################################
#WRITE METHOD
# file = open("sample1.txt", "w") 
# file.write("Hello, World!") 
# file.close() 

#writeline method
# file=open("sample1.txt","w")
# line=["Hello\n", "Welcome to Python file handling\n"]
# file.writelines(line)
# file.close()


###################33
#append method
# file=open("sample1.txt","a")
# file.write("append last")
# file.close()

#with statement
# with open("sample1.txt","r") as file:
#     content=file.read()
#     print(content)


#######
#tell :find docs cursor position
# with open("sample.txt","r") as file:
#     content=file.read()
#     length=file.tell()
#     print(content)
#     print(length)


#seek method: moves the file cursor to a specified position. 
with open("sample.txt","r") as file:
    file.seek(4)
    print(file.read())
    