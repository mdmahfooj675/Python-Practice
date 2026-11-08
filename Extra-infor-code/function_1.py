# learn and practice some question based on the function in python


# question 1-> Greeting: ek function banao jo name parameter le aur Hello, <name>! print kare
print("1-> take name as input and print the greeting using function")

def greet_name(name):
    print("hello" , name)

Name = input("enter your beautiful name : ")
greet_name(Name)

print("problem solved seccessfully....")


# creat a function that check wheather a number is even or odd
print("9-> creat a function that check given number is even or odd")

def check_num(x):
    if x % 2 == 0:
        print("even number : " , x)
    else:
        print("odd number : " , x)

Num = int(input("Enter a number : "))
check_num(Num)

print("code execution successfully....")

#----------------------------------------------------------------------------------
#creat a function that find the factorial of n (n as a parameters)
print("8-> creat a function that find the factorial of n (n as a parameters) , take n as input foem the user")

def calc_factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print("factorial of the number " , n , ": " ,  fact)

num = int(input("enter a number : "))
calc_factorial(num)

print("problem executed successfully.....")

# ----------------------------------------------------------------------------------
# creat a function that convert the USD to INR
print("7-> creat a function that convert the USD to INR")

def usd_inr(usd_val):
    inr_val = usd_val * 93.89
    print(usd_val , "$ " , "=" , inr_val , "rs")

usd_inr(100)
print("problem executed successfully.....")

# ----------------------------------------------------------------------------------
# creat a function that find the factorial of n (n as a parameters)
print("6-> creat a function that find the factorial of n (n as a parameters)")

def calc_factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print("factorial of the number " , n , ": " ,  fact)

calc_factorial(5)

print("problem executed successfully.....")

# ----------------------------------------------------------------------------------
# creat a function to print the elements in the list in a single line (list as a parameters)
print("5-> creat a function to print the elements in the list in a single line (list as a parameters) ")

city = ["gomia" , "bhopal" , "mumbai" , "pune" , "delhi"]
name = ["mohan" , "sohan" , "ajay" , "vijay" , "mukesh" , "ramesh"]

def print_list(list):
    for item in list:
        print(item , end = "  ")
    print()

print_list(city)
print_list(name)


print("problem executed successfully.....")

# ----------------------------------------------------------------------------------
# creat a function that calculate the length of the list (list as a parameters)
print("4-> creat a function that print the length of the list (list as a parameters)")

city = ["gomia" , "bhopal" , "mumbai" , "pune" , "delhi"]
name = ["mohan" , "sohan" , "ajay" , "vijay" , "mukesh" , "ramesh"]

def len_list(list):
    print("length of the list : " , len(list))

len_list(city)
len_list(name)

print("problem solved successfully...")

# ----------------------------------------------------------------------------------
# creat a function that calculate the average of three numbers

print("3-> creat a function that calculate the average of three numbers ")

def calc_average(x , y , z):
    avg = (x + y + z) / 3
    print("average of three numbers : " , avg)
    return avg

calc_average(10 , 20 , 30)
print("code execution completed....")

# ----------------------------------------------------------------------------------
# creat a function that  perform the addition operation

# this is called the function definition
print("2-> creat a function that calculate the addition operation")
def calculate_sum(a , b):  # a & b are called the parameters of the function
    sum = a + b
    print(sum)
    return sum

# this line is called the function call
calculate_sum(45 , 67) # values like 45 & 67 are called the parameters
print("code execuion successfully....")

# ----------------------------------------------------------------------------------
# we can creat a function without an argument , parameters and return
# here is the example
print("1-> creat a function that print the string without any parameters and return type")
def print_mahfooj():
    print("hello mahfooj")

output = print_mahfooj() # without parameters function return the none value
print(output) 
print("code execution successfully...")
# ----------------------------------------------------------------------------------