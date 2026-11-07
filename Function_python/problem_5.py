# creat a function to print the elements in the list in a single line (list as a parameters)

print("question -> creat a function to print the elements in the list in a single line (list as a parameters) ")

city = ["gomia" , "bhopal" , "mumbai" , "pune" , "delhi"]
name = ["mohan" , "sohan" , "ajay" , "vijay" , "mukesh" , "ramesh"]

def print_list(list):
    for item in list:
        print(item , end = "  ")
    print()

print_list(city)
print_list(name)


print("problem executed successfully.....")
