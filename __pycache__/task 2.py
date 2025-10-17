filename = input("Enter filename to read: ")
try:
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found.")
